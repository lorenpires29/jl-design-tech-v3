import django.db.models.deletion
import django.core.validators
from django.db import migrations,models
class Migration(migrations.Migration):
 initial=True
 dependencies=[]
 operations=[
  migrations.CreateModel(name="Servico",fields=[("id",models.BigAutoField(primary_key=True,serialize=False)),("nome",models.CharField(max_length=160)),("slug",models.SlugField(unique=True)),("resumo",models.CharField(max_length=240)),("descricao",models.TextField()),("imagem",models.ImageField(blank=True,upload_to="servicos/")),("ativo",models.BooleanField(default=True)),("ordem",models.PositiveIntegerField(default=0))],options={"ordering":["ordem","nome"]}),
  migrations.CreateModel(name="SolicitacaoOrcamento",fields=[("id",models.BigAutoField(primary_key=True,serialize=False)),("nome",models.CharField(max_length=150)),("email",models.EmailField(max_length=254)),("telefone",models.CharField(blank=True,max_length=30)),("descricao",models.TextField(max_length=5000)),("quantidade",models.PositiveIntegerField(default=1)),("prazo_desejado",models.DateField(blank=True,null=True)),("referencia",models.FileField(blank=True,upload_to="orcamentos/referencias/",validators=[django.core.validators.FileExtensionValidator(["png","jpg","jpeg","pdf"])])),("status",models.CharField(choices=[("nova","Nova"),("analise","Em análise"),("respondida","Respondida"),("concluida","Concluída"),("cancelada","Cancelada")],default="nova",max_length=12)),("observacoes_internas",models.TextField(blank=True)),("arquivada",models.BooleanField(default=False)),("criada_em",models.DateTimeField(auto_now_add=True)),("atualizada_em",models.DateTimeField(auto_now=True)),("servico",models.ForeignKey(on_delete=django.db.models.deletion.PROTECT,related_name="solicitacoes",to="servicos.servico"))],options={"ordering":["-criada_em"]})
 ]
