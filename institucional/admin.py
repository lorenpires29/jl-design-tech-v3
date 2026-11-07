from django.contrib import admin
from .models import MensagemContato
@admin.register(MensagemContato)
class MensagemContatoAdmin(admin.ModelAdmin):
 list_display=("nome","email","criada_em","lida")
 list_filter=("lida","criada_em")
 search_fields=("nome","email","mensagem")
 readonly_fields=("nome","email","mensagem","criada_em")
