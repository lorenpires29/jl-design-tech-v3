from urllib.parse import urlsplit
from django.core.exceptions import ValidationError
from django.db import models

def validar_link_parceiro(url):
 p=urlsplit(url)
 host=(p.hostname or "").lower()
 allowed=("shopee.com.br","shopee.com","mercadolivre.com.br","mercadolivre.com","mercadopago.com.br","collshp.com")
 if p.scheme!="https" or not host or p.username or p.password or p.port not in (None,443) or not any(host==domain or host.endswith("."+domain) for domain in allowed):
  raise ValidationError("Use um link HTTPS de parceiro autorizado (Shopee, Mercado Livre ou Collshp).")

class Parceiro(models.Model):
 nome=models.CharField(max_length=120,unique=True)
 slug=models.SlugField(unique=True)
 ativo=models.BooleanField(default=True)
 def __str__(self): return self.nome

class CategoriaAfiliado(models.Model):
 nome=models.CharField(max_length=120,unique=True)
 slug=models.SlugField(unique=True)
 ativa=models.BooleanField(default=True)
 def __str__(self): return self.nome

class ProdutoAfiliado(models.Model):
 class Revisao(models.TextChoices):
  PENDENTE="pendente","Pendente"
  APROVADO="aprovado","Aprovado"
  REJEITADO="rejeitado","Rejeitado"
 parceiro=models.ForeignKey(Parceiro,on_delete=models.PROTECT)
 categoria=models.ForeignKey(CategoriaAfiliado,on_delete=models.PROTECT)
 nome=models.CharField(max_length=180)
 slug=models.SlugField(unique=True)
 descricao=models.TextField(blank=True)
 imagem=models.ImageField(upload_to="maker_store/",blank=True)
 url_destino=models.URLField(max_length=2000,validators=[validar_link_parceiro])
 preco_informativo=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
 status_revisao=models.CharField(max_length=10,choices=Revisao.choices,default=Revisao.PENDENTE)
 ativo=models.BooleanField(default=False)
 destaque=models.BooleanField(default=False)
 criado_em=models.DateTimeField(auto_now_add=True)
 class Meta:
  ordering=["-destaque","-criado_em"]
 def clean(self):
  super().clean()
  validar_link_parceiro(self.url_destino)
  if self.ativo and self.status_revisao!=self.Revisao.APROVADO:
   raise ValidationError({"ativo":"Apenas produtos aprovados podem ser publicados."})
 def save(self,*args,**kwargs):
  self.full_clean()
  return super().save(*args,**kwargs)
 def __str__(self): return self.nome

class CliqueAfiliado(models.Model):
 produto=models.ForeignKey(ProdutoAfiliado,on_delete=models.CASCADE,related_name="cliques")
 criado_em=models.DateTimeField(auto_now_add=True)
 class Meta:
  ordering=["-criado_em"]
