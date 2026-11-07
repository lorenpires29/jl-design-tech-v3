from django.contrib import admin
from .models import ConexaoShopee,VinculoAnuncio,ExecucaoSincronizacao
@admin.register(ConexaoShopee)
class ConexaoShopeeAdmin(admin.ModelAdmin):
 list_display=("nome","identificador_loja","status","ultima_sincronizacao")
 search_fields=("nome","identificador_loja")
 list_filter=("status",)
 readonly_fields=("ultima_sincronizacao","atualizada_em")
 def get_readonly_fields(self,request,obj=None):
  return ("ultima_sincronizacao","atualizada_em","status") if obj else ("ultima_sincronizacao","atualizada_em","status")
@admin.register(VinculoAnuncio)
class VinculoAnuncioAdmin(admin.ModelAdmin):
 list_display=("conexao","produto","anuncio_externo_id","ativo")
 list_filter=("ativo","conexao")
 search_fields=("anuncio_externo_id","produto__nome")
 autocomplete_fields=("produto",)
@admin.register(ExecucaoSincronizacao)
class ExecucaoSincronizacaoAdmin(admin.ModelAdmin):
 list_display=("conexao","origem","status","total_registros","criada_em","finalizada_em")
 list_filter=("status","origem")
 readonly_fields=("conexao","origem","status","total_registros","detalhes","criada_em","finalizada_em")
 def has_add_permission(self,request): return False
 def has_change_permission(self,request,obj=None): return False
 def has_delete_permission(self,request,obj=None): return False
