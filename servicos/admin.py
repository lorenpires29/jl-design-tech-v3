from django.contrib import admin
from .models import Servico,SolicitacaoOrcamento
@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
 list_display=("nome","ativo","ordem")
 list_filter=("ativo",)
 search_fields=("nome","descricao")
 prepopulated_fields={"slug":("nome",)}
@admin.register(SolicitacaoOrcamento)
class SolicitacaoAdmin(admin.ModelAdmin):
 list_display=("id","nome","servico","status","arquivada","criada_em")
 list_filter=("status","arquivada","servico","criada_em")
 search_fields=("nome","email","descricao")
 readonly_fields=("nome","email","telefone","servico","descricao","quantidade","prazo_desejado","referencia","criada_em","atualizada_em")
 fields=("nome","email","telefone","servico","descricao","quantidade","prazo_desejado","referencia","status","observacoes_internas","arquivada","criada_em","atualizada_em")
 actions=("arquivar","desarquivar")
 @admin.action(description="Arquivar solicitações selecionadas")
 def arquivar(self,request,queryset): queryset.update(arquivada=True)
 @admin.action(description="Desarquivar solicitações selecionadas")
 def desarquivar(self,request,queryset): queryset.update(arquivada=False)
 def has_add_permission(self,request): return False
