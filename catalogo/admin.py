from django.contrib import admin
from .models import Categoria,Produto,AnuncioShopee
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
 list_display=("nome","ativa")
 prepopulated_fields={"slug":("nome",)}
class AnuncioInline(admin.TabularInline):
 model=AnuncioShopee
 extra=1
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
 list_display=("nome","categoria","ativo","destaque")
 list_filter=("ativo","categoria")
 prepopulated_fields={"slug":("nome",)}
 inlines=[AnuncioInline]
