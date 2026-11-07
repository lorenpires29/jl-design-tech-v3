from django.contrib import admin
from .models import Parceiro,CategoriaAfiliado,ProdutoAfiliado,CliqueAfiliado
@admin.register(Parceiro)
class ParceiroAdmin(admin.ModelAdmin):
 list_display=("nome","ativo")
 prepopulated_fields={"slug":("nome",)}
@admin.register(CategoriaAfiliado)
class CategoriaAfiliadoAdmin(admin.ModelAdmin):
 list_display=("nome","ativa")
 prepopulated_fields={"slug":("nome",)}
@admin.register(ProdutoAfiliado)
class ProdutoAfiliadoAdmin(admin.ModelAdmin):
 list_display=("nome","parceiro","categoria","status_revisao","ativo","destaque")
 list_filter=("status_revisao","ativo","destaque","parceiro","categoria")
 search_fields=("nome","descricao")
 prepopulated_fields={"slug":("nome",)}
@admin.register(CliqueAfiliado)
class CliqueAfiliadoAdmin(admin.ModelAdmin):
 list_display=("produto","criado_em")
 readonly_fields=("produto","criado_em")
 def has_add_permission(self,request): return False
 def has_change_permission(self,request,obj=None): return False
 def has_delete_permission(self,request,obj=None): return False
