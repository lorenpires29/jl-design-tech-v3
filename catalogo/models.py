from urllib.parse import urlsplit
from django.core.exceptions import ValidationError
from django.db import models
class Categoria(models.Model):
 nome=models.CharField(max_length=100,unique=True)
 slug=models.SlugField(unique=True)
 ativa=models.BooleanField(default=True)
 def __str__(self): return self.nome
class Produto(models.Model):
 categoria=models.ForeignKey(Categoria,on_delete=models.PROTECT)
 nome=models.CharField(max_length=180)
 slug=models.SlugField(unique=True)
 descricao=models.TextField()
 imagem=models.ImageField(upload_to="produtos/",blank=True)
 preco_referencia=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
 ativo=models.BooleanField(default=True)
 destaque=models.BooleanField(default=False)
 criado_em=models.DateTimeField(auto_now_add=True)
 class Meta:
  ordering=["-criado_em"]
 def __str__(self): return self.nome
class AnuncioShopee(models.Model):
 produto=models.ForeignKey(Produto,on_delete=models.CASCADE,related_name="anuncios")
 url=models.URLField(max_length=2000)
 ativo=models.BooleanField(default=True)
 def clean(self):
  p=urlsplit(self.url)
  host=(p.hostname or "").lower()
  if p.scheme!="https" or p.username or p.password or p.port not in (None,443) or not (host in ("shopee.com.br","shopee.com") or host.endswith(".shopee.com.br") or host.endswith(".shopee.com")):
   raise ValidationError({"url":"Use um link HTTPS da Shopee."})
 def save(self,*args,**kwargs):
  self.full_clean()
  return super().save(*args,**kwargs)

class CliqueAnuncio(models.Model):
 anuncio=models.ForeignKey(AnuncioShopee,on_delete=models.CASCADE,related_name="cliques")
 criado_em=models.DateTimeField(auto_now_add=True)
 class Meta:
  ordering=["-criado_em"]
