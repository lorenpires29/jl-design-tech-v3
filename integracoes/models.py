from django.db import models
from django.core.exceptions import ValidationError
from catalogo.models import Produto

class ConexaoShopee(models.Model):
 nome=models.CharField(max_length=120,unique=True)
 identificador_loja=models.CharField(max_length=120,blank=True)
 status=models.CharField(max_length=20,choices=[("nao_configurada","Não configurada"),("pendente","Pendente"),("autorizada","Autorizada"),("revogada","Revogada"),("erro","Erro")],default="nao_configurada")
 ultima_sincronizacao=models.DateTimeField(null=True,blank=True)
 atualizada_em=models.DateTimeField(auto_now=True)
 def __str__(self): return self.nome

class VinculoAnuncio(models.Model):
 conexao=models.ForeignKey(ConexaoShopee,on_delete=models.PROTECT,related_name="vinculos")
 produto=models.ForeignKey(Produto,on_delete=models.PROTECT)
 anuncio_externo_id=models.CharField(max_length=120)
 ativo=models.BooleanField(default=True)
 class Meta:
  constraints=[models.UniqueConstraint(fields=["conexao","anuncio_externo_id"],name="uq_vinculo_shopee_loja_anuncio")]
 def clean(self):
  if self.ativo and self.conexao_id and self.conexao.status!="autorizada":
   raise ValidationError({"ativo":"A loja precisa estar autorizada antes de ativar o vínculo."})
 def __str__(self): return f"{self.conexao}: {self.anuncio_externo_id}"

class ExecucaoSincronizacao(models.Model):
 conexao=models.ForeignKey(ConexaoShopee,on_delete=models.PROTECT,related_name="execucoes")
 origem=models.CharField(max_length=20,choices=[("api","API"),("arquivo","Arquivo")])
 status=models.CharField(max_length=20,choices=[("pendente","Pendente"),("processando","Processando"),("concluida","Concluída"),("falha","Falha")],default="pendente")
 total_registros=models.PositiveIntegerField(default=0)
 detalhes=models.TextField(blank=True)
 criada_em=models.DateTimeField(auto_now_add=True)
 finalizada_em=models.DateTimeField(null=True,blank=True)
 class Meta:
  ordering=["-criada_em"]
 def __str__(self): return f"{self.conexao} — {self.status}"
