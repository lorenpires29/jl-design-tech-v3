from django.db import models
class MensagemContato(models.Model):
 nome=models.CharField(max_length=150)
 email=models.EmailField()
 mensagem=models.TextField(max_length=5000)
 criada_em=models.DateTimeField(auto_now_add=True)
 lida=models.BooleanField(default=False)
 class Meta:
  ordering=["-criada_em"]
 def __str__(self): return self.nome
