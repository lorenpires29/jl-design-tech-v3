from django.db import models
from integracoes.models import ConexaoShopee

class PedidoExterno(models.Model):
 conexao=models.ForeignKey(ConexaoShopee,on_delete=models.PROTECT,related_name="pedidos")
 identificador_externo=models.CharField(max_length=120)
 status_externo=models.CharField(max_length=100,blank=True)
 total=models.DecimalField(max_digits=12,decimal_places=2,null=True,blank=True)
 moeda=models.CharField(max_length=3,default="BRL")
 data_pedido=models.DateTimeField(null=True,blank=True)
 sincronizado_em=models.DateTimeField(auto_now=True)
 divergente=models.BooleanField(default=False)
 class Meta:
  constraints=[models.UniqueConstraint(fields=["conexao","identificador_externo"],name="uq_pedido_loja_externo")]
  ordering=["-sincronizado_em"]
 def __str__(self): return self.identificador_externo

class ItemPedido(models.Model):
 pedido=models.ForeignKey(PedidoExterno,on_delete=models.CASCADE,related_name="itens")
 identificador_produto=models.CharField(max_length=120,blank=True)
 descricao=models.CharField(max_length=240)
 quantidade=models.PositiveIntegerField()
 preco_unitario=models.DecimalField(max_digits=12,decimal_places=2)
 def __str__(self): return self.descricao

class HistoricoStatusPedido(models.Model):
 pedido=models.ForeignKey(PedidoExterno,on_delete=models.CASCADE,related_name="historico")
 status_anterior=models.CharField(max_length=100,blank=True)
 status_novo=models.CharField(max_length=100)
 origem=models.CharField(max_length=20,choices=[("api","API"),("arquivo","Arquivo"),("sistema","Sistema")])
 registrado_em=models.DateTimeField(auto_now_add=True)
 class Meta:
  ordering=["-registrado_em"]
