from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import SolicitacaoOrcamento,Servico

class SolicitacaoForm(forms.ModelForm):
 class Meta:
  model=SolicitacaoOrcamento
  fields=("nome","email","telefone","servico","descricao","quantidade","prazo_desejado","referencia")
  widgets={"prazo_desejado":forms.DateInput(attrs={"type":"date"}),"descricao":forms.Textarea(attrs={"rows":5})}
 def __init__(self,*args,**kwargs):
  super().__init__(*args,**kwargs)
  self.fields["servico"].queryset=Servico.objects.filter(ativo=True)
  self.fields["referencia"].help_text="PNG, JPG ou PDF; até 5 MB."
 def clean_descricao(self):
  value=self.cleaned_data["descricao"].strip()
  if len(value)<15: raise ValidationError("Descreva seu projeto com pelo menos 15 caracteres.")
  return value
 def clean_prazo_desejado(self):
  value=self.cleaned_data.get("prazo_desejado")
  if value and value<timezone.localdate(): raise ValidationError("Informe uma data futura.")
  return value
 def clean_referencia(self):
  value=self.cleaned_data.get("referencia")
  if not value: return value
  if value.size>5*1024*1024: raise ValidationError("O arquivo deve ter no máximo 5 MB.")
  pos=value.tell()
  header=value.read(12)
  value.seek(pos)
  ext=value.name.lower().rsplit(".",1)[-1]
  valid={"png":header.startswith(b"\x89PNG\r\n\x1a\n"),"jpg":header.startswith(b"\xff\xd8\xff"),"jpeg":header.startswith(b"\xff\xd8\xff"),"pdf":header.startswith(b"%PDF-")}
  if not valid.get(ext,False): raise ValidationError("O conteúdo do arquivo não corresponde ao formato informado.")
  return value
