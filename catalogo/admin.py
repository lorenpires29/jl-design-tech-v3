from django.contrib import admin,messages
from django.core.exceptions import ValidationError
from django.db.models import Count
from django.utils.html import format_html
from .models import Categoria,Produto,AnuncioShopee,CliqueAnuncio

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
 list_display=("nome","slug","ativa","quantidade_produtos")
 list_filter=("ativa",)
 search_fields=("nome","slug")
 prepopulated_fields={"slug":("nome",)}
 actions=("ativar","desativar")
 def get_queryset(self,request):
  return super().get_queryset(request).annotate(total_produtos=Count("produto"))
 @admin.display(description="Produtos",ordering="total_produtos")
 def quantidade_produtos(self,obj): return obj.total_produtos
 @admin.action(description="Ativar categorias selecionadas")
 def ativar(self,request,queryset): queryset.update(ativa=True)
 @admin.action(description="Desativar categorias selecionadas")
 def desativar(self,request,queryset): queryset.update(ativa=False)

class AnuncioInline(admin.TabularInline):
 model=AnuncioShopee
 extra=0
 fields=("url","ativo")
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
 list_display=("nome","categoria","preco_referencia","ativo","destaque","quantidade_anuncios","criado_em")
 list_filter=("ativo","destaque","categoria","criado_em")
 search_fields=("nome","descricao","slug")
 prepopulated_fields={"slug":("nome",)}
 readonly_fields=("criado_em","imagem_preview")
 fields=("nome","slug","categoria","descricao","imagem","imagem_preview","preco_referencia","ativo","destaque","criado_em")
 inlines=[AnuncioInline]
 actions=("publicar","despublicar","destacar","retirar_destaque")
 list_per_page=30
 def get_queryset(self,request):
  return super().get_queryset(request).annotate(total_anuncios=Count("anuncios"))
 @admin.display(description="Anúncios",ordering="total_anuncios")
 def quantidade_anuncios(self,obj): return obj.total_anuncios
 @admin.display(description="Imagem")
 def imagem_preview(self,obj):
  return format_html('<img src="{}" alt="Prévia" style="max-width:180px;max-height:180px;border-radius:10px">',obj.imagem.url) if obj.pk and obj.imagem else "Sem imagem"
 @admin.action(description="Publicar produtos selecionados")
 def publicar(self,request,queryset):
  ok=0
  for produto in queryset.select_related("categoria"):
   if not produto.categoria.ativa:
    self.message_user(request,f"Categoria inativa: {produto.nome}",level=messages.WARNING)
    continue
   produto.ativo=True
   try: produto.full_clean();produto.save(update_fields=["ativo"]);ok+=1
   except ValidationError as exc: self.message_user(request,str(exc),level=messages.ERROR)
  self.message_user(request,f"{ok} produto(s) publicado(s).")
 @admin.action(description="Despublicar produtos selecionados")
 def despublicar(self,request,queryset): self.message_user(request,f'{queryset.update(ativo=False)} produto(s) despublicado(s).')
 @admin.action(description="Destacar produtos selecionados")
 def destacar(self,request,queryset): self.message_user(request,f'{queryset.update(destaque=True)} produto(s) destacado(s).')
 @admin.action(description="Retirar destaque")
 def retirar_destaque(self,request,queryset): self.message_user(request,f'{queryset.update(destaque=False)} destaque(s) removido(s).')

@admin.register(AnuncioShopee)
class AnuncioShopeeAdmin(admin.ModelAdmin):
 list_display=("produto","url","ativo","total_cliques")
 list_filter=("ativo",)
 search_fields=("produto__nome","url")
 autocomplete_fields=("produto",)
 actions=("ativar","desativar")
 def get_queryset(self,request): return super().get_queryset(request).annotate(total=Count("cliques"))
 @admin.display(description="Cliques",ordering="total")
 def total_cliques(self,obj): return obj.total
 @admin.action(description="Ativar anúncios")
 def ativar(self,request,queryset):
  ok=0
  for anuncio in queryset:
   anuncio.ativo=True
   try: anuncio.full_clean();anuncio.save(update_fields=["ativo"]);ok+=1
   except ValidationError as exc: self.message_user(request,str(exc),level=messages.ERROR)
  self.message_user(request,f"{ok} anúncio(s) ativado(s).")
 @admin.action(description="Desativar anúncios")
 def desativar(self,request,queryset): queryset.update(ativo=False)

@admin.register(CliqueAnuncio)
class CliqueAnuncioAdmin(admin.ModelAdmin):
 list_display=("anuncio","criado_em")
 list_filter=("criado_em",)
 readonly_fields=("anuncio","criado_em")
 def has_add_permission(self,request): return False
 def has_change_permission(self,request,obj=None): return False
 def has_delete_permission(self,request,obj=None): return False
