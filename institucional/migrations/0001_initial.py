from django.db import migrations,models
class Migration(migrations.Migration):
 initial=True
 dependencies=[]
 operations=[migrations.CreateModel(name="MensagemContato",fields=[("id",models.BigAutoField(primary_key=True,serialize=False)),("nome",models.CharField(max_length=150)),("email",models.EmailField(max_length=254)),("mensagem",models.TextField(max_length=5000)),("criada_em",models.DateTimeField(auto_now_add=True)),("lida",models.BooleanField(default=False))],options={"ordering":["-criada_em"]})]
