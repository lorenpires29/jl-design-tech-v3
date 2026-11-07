from django.db import models
from django.core.validators import FileExtensionValidator

class Servico(models.Model):
 nome=models.CharField(max_length=160)
 slug=models.SlugField(unique=True)
 resumo=models.CharField(max_length=240)
 descricao=models.TextField()
 imagem=models.ImageField(upload_to="servicos/",blank=True)
 ativo=models.BooleanField(default=True)
 ordem=models.PositiveIntegerField(default=0)
 class Meta:
  ordering=["ordem","nome"]
 def __str__(self): return self.nome

class SolicitacaoOrcamento(models.Model):
 class Status(models.TextChoices):
  NOVA="nova","Nova"
  ANALISE="analise","Em análise"
  RESPONDIDA="respondida","Respondida"
  CONCLUIDA="concluida","Concluída"
  CANCELADA="cancelada","Cancelada"
 nome=models.CharField(max_length=150)
 email=models.EmailField()
 telefone=models.CharField(max_length=30,blank=True)
 servico=models.ForeignKey(Servico,on_delete=models.PROTECT,related_name="solicitacoes")
 descricao=models.TextField(max_length=5000)
 quantidade=models.PositiveIntegerField(default=1)
 prazo_desejado=models.DateField(null=True,blank=True)
 referencia=models.FileField(upload_to="orcamentos/referencias/",blank=True,validators=[FileExtensionValidator(["png","jpg","jpeg","pdf"])])
 status=models.CharField(max_length=12,choices=Status.choices,default=Status.NOVA)
 observacoes_internas=models.TextField(blank=True)
 arquivada=models.BooleanField(default=False)
 criada_em=models.DateTimeField(auto_now_add=True)
 atualizada_em=models.DateTimeField(auto_now=True)
 class Meta:
  ordering=["-criada_em"]
 def __str__(self): return f"#{self.pk} — {self.nome}"
