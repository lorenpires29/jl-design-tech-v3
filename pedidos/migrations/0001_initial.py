import django.db.models.deletion
from django.db import migrations,models
class Migration(migrations.Migration):
 initial=True
 dependencies=[("integracoes","0001_initial")]
 operations=[
  migrations.CreateModel(name="PedidoExterno",fields=[("id",models.BigAutoField(primary_key=True,serialize=False)),("identificador_externo",models.CharField(max_length=120)),("status_externo",models.CharField(max_length=100,blank=True)),("total",models.DecimalField(max_digits=12,decimal_places=2,null=True,blank=True)),("moeda",models.CharField(max_length=3,default="BRL")),("data_pedido",models.DateTimeField(null=True,blank=True)),("sincronizado_em",models.DateTimeField(auto_now=True)),("divergente",models.BooleanField(default=False)),("conexao",models.ForeignKey(on_delete=django.db.models.deletion.PROTECT,related_name="pedidos",to="integracoes.conexaoshopee"))],options={"ordering":["-sincronizado_em"]}),
  migrations.AddConstraint(model_name="pedidoexterno",constraint=models.UniqueConstraint(fields=("conexao","identificador_externo"),name="uq_pedido_loja_externo")),
  migrations.CreateModel(name="ItemPedido",fields=[("id",models.BigAutoField(primary_key=True,serialize=False)),("identificador_produto",models.CharField(max_length=120,blank=True)),("descricao",models.CharField(max_length=240)),("quantidade",models.PositiveIntegerField()),("preco_unitario",models.DecimalField(max_digits=12,decimal_places=2)),("pedido",models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,related_name="itens",to="pedidos.pedidoexterno"))]),
  migrations.CreateModel(name="HistoricoStatusPedido",fields=[("id",models.BigAutoField(primary_key=True,serialize=False)),("status_anterior",models.CharField(max_length=100,blank=True)),("status_novo",models.CharField(max_length=100)),("origem",models.CharField(max_length=20,choices=[("api","API"),("arquivo","Arquivo"),("sistema","Sistema")])),("registrado_em",models.DateTimeField(auto_now_add=True)),("pedido",models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,related_name="historico",to="pedidos.pedidoexterno"))],options={"ordering":["-registrado_em"]})
 ]
