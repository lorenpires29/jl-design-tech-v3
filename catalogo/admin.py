from django.contrib import admin
from .models import Categoria,Produto,AnuncioShopee,CliqueAnuncio
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
 list_display=("nome","ativa")
 list_filter=("ativa",)
 search_fields=("nome",)
 prepopulated_fields={"slug":("nome",)}
class AnuncioInline(admin.TabularInline):
 model=AnuncioShopee
 extra=1
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
 list_display=("nome","categoria","preco_referencia","ativo","destaque")
 list_filter=("ativo","destaque","categoria")
 search_fields=("nome","descricao")
 prepopulated_fields={"slug":("nome",)}
 inlines=[AnuncioInline]
@admin.register(CliqueAnuncio)
class CliqueAnuncioAdmin(admin.ModelAdmin):
 list_display=("anuncio","criado_em")
 readonly_fields=("anuncio","criado_em")
 def has_add_permission(self,request): return False
 def has_change_permission(self,request,obj=None): return False
 def has_delete_permission(self,request,obj=None): return False
