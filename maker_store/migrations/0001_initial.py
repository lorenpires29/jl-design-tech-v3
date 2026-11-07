import django.db.models.deletion
from django.db import migrations,models
import maker_store.models
class Migration(migrations.Migration):
 initial=True
 dependencies=[]
 operations=[
  migrations.CreateModel(name="Parceiro",fields=[("id",models.BigAutoField(primary_key=True,serialize=False)),("nome",models.CharField(max_length=120,unique=True)),("slug",models.SlugField(unique=True)),("ativo",models.BooleanField(default=True))]),
  migrations.CreateModel(name="CategoriaAfiliado",fields=[("id",models.BigAutoField(primary_key=True,serialize=False)),("nome",models.CharField(max_length=120,unique=True)),("slug",models.SlugField(unique=True)),("ativa",models.BooleanField(default=True))]),
  migrations.CreateModel(name="ProdutoAfiliado",fields=[("id",models.BigAutoField(primary_key=True,serialize=False)),("nome",models.CharField(max_length=180)),("slug",models.SlugField(unique=True)),("descricao",models.TextField(blank=True)),("imagem",models.ImageField(blank=True,upload_to="maker_store/")),("url_destino",models.URLField(max_length=2000,validators=[maker_store.models.validar_link_parceiro])),("preco_informativo",models.DecimalField(blank=True,decimal_places=2,max_digits=10,null=True)),("status_revisao",models.CharField(choices=[("pendente","Pendente"),("aprovado","Aprovado"),("rejeitado","Rejeitado")],default="pendente",max_length=10)),("ativo",models.BooleanField(default=False)),("destaque",models.BooleanField(default=False)),("criado_em",models.DateTimeField(auto_now_add=True)),("parceiro",models.ForeignKey(on_delete=django.db.models.deletion.PROTECT,to="maker_store.parceiro")),("categoria",models.ForeignKey(on_delete=django.db.models.deletion.PROTECT,to="maker_store.categoriaafiliado"))],options={"ordering":["-destaque","-criado_em"]}),
  migrations.CreateModel(name="CliqueAfiliado",fields=[("id",models.BigAutoField(primary_key=True,serialize=False)),("criado_em",models.DateTimeField(auto_now_add=True)),("produto",models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,related_name="cliques",to="maker_store.produtoafiliado"))],options={"ordering":["-criado_em"]})
 ]
