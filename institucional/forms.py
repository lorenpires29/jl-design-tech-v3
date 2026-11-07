from django import forms
from .models import MensagemContato
class ContatoForm(forms.ModelForm):
 class Meta:
  model=MensagemContato
  fields=("nome","email","mensagem")
 def clean_mensagem(self):
  msg=self.cleaned_data["mensagem"].strip()
  if len(msg)<10: raise forms.ValidationError("Escreva pelo menos dez caracteres.")
  return msg
