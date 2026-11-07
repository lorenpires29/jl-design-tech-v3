import django.db.models.deletion
from django.db import migrations,models
class Migration(migrations.Migration):
 initial=True
 dependencies=[("catalogo","0002_cliqueanuncio")]
 operations=[
  migrations.CreateModel(name="ConexaoShopee",fields=[("id",models.BigAutoField(primary_key=True,serialize=False)),("nome",models.CharField(max_length=120,unique=True)),("identificador_loja",models.CharField(max_length=120,blank=True)),("status",models.CharField(max_length=20,choices=[("nao_configurada","Não configurada"),("pendente","Pendente"),("autorizada","Autorizada"),("revogada","Revogada"),("erro","Erro")],default="nao_configurada")),("ultima_sincronizacao",models.DateTimeField(null=True,blank=True)),("atualizada_em",models.DateTimeField(auto_now=True))]),
  migrations.CreateModel(name="VinculoAnuncio",fields=[("id",models.BigAutoField(primary_key=True,serialize=False)),("anuncio_externo_id",models.CharField(max_length=120)),("ativo",models.BooleanField(default=True)),("conexao",models.ForeignKey(on_delete=django.db.models.deletion.PROTECT,related_name="vinculos",to="integracoes.conexaoshopee")),("produto",models.ForeignKey(on_delete=django.db.models.deletion.PROTECT,to="catalogo.produto"))]),
  migrations.AddConstraint(model_name="vinculoanuncio",constraint=models.UniqueConstraint(fields=("conexao","anuncio_externo_id"),name="uq_vinculo_shopee_loja_anuncio")),
  migrations.CreateModel(name="ExecucaoSincronizacao",fields=[("id",models.BigAutoField(primary_key=True,serialize=False)),("origem",models.CharField(max_length=20,choices=[("api","API"),("arquivo","Arquivo")])),("status",models.CharField(max_length=20,choices=[("pendente","Pendente"),("processando","Processando"),("concluida","Concluída"),("falha","Falha")],default="pendente")),("total_registros",models.PositiveIntegerField(default=0)),("detalhes",models.TextField(blank=True)),("criada_em",models.DateTimeField(auto_now_add=True)),("finalizada_em",models.DateTimeField(null=True,blank=True)),("conexao",models.ForeignKey(on_delete=django.db.models.deletion.PROTECT,related_name="execucoes",to="integracoes.conexaoshopee"))],options={"ordering":["-criada_em"]})
 ]
