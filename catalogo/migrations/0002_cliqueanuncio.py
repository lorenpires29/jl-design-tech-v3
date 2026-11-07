import django.db.models.deletion
from django.db import migrations,models
class Migration(migrations.Migration):
 dependencies=[("catalogo","0001_initial")]
 operations=[migrations.CreateModel(name="CliqueAnuncio",fields=[("id",models.BigAutoField(primary_key=True,serialize=False)),("criado_em",models.DateTimeField(auto_now_add=True)),("anuncio",models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,related_name="cliques",to="catalogo.anuncioshopee"))],options={"ordering":["-criado_em"]})]
