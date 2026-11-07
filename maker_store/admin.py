from django.contrib import admin,messages
from django.core.exceptions import ValidationError
from django.db.models import Count
from django.utils.html import format_html
from .models import Parceiro,CategoriaAfiliado,ProdutoAfiliado,CliqueAfiliado

@admin.register(Parceiro)
class ParceiroAdmin(admin.ModelAdmin):
 list_display=("nome","ativo","quantidade_ofertas")
 list_filter=("ativo",)
 search_fields=("nome",)
 prepopulated_fields={"slug":("nome",)}
 def get_queryset(self,request): return super().get_queryset(request).annotate(total=Count("produtoafiliado"))
 @admin.display(description="Ofertas",ordering="total")
 def quantidade_ofertas(self,obj): return obj.total

@admin.register(CategoriaAfiliado)
class CategoriaAfiliadoAdmin(admin.ModelAdmin):
 list_display=("nome","ativa","quantidade_ofertas")
 list_filter=("ativa",)
 search_fields=("nome",)
 prepopulated_fields={"slug":("nome",)}
 def get_queryset(self,request): return super().get_queryset(request).annotate(total=Count("produtoafiliado"))
 @admin.display(description="Ofertas",ordering="total")
 def quantidade_ofertas(self,obj): return obj.total

@admin.register(ProdutoAfiliado)
class ProdutoAfiliadoAdmin(admin.ModelAdmin):
 list_display=("nome","parceiro","categoria","status_revisao","ativo","destaque","total_cliques","situacao_link")
 list_filter=("status_revisao","ativo","destaque","parceiro","categoria")
 search_fields=("nome","descricao","slug","url_destino")
 prepopulated_fields={"slug":("nome",)}
 readonly_fields=("criado_em","imagem_preview","total_cliques")
 fields=("nome","slug","parceiro","categoria","descricao","imagem","imagem_externa","imagem_preview","url_destino","preco_informativo","status_revisao","ativo","destaque","total_cliques","criado_em")
 actions=("aprovar","rejeitar","despublicar","destacar","retirar_destaque")
 list_per_page=30
 def get_queryset(self,request): return super().get_queryset(request).annotate(total=Count("cliques"))
 @admin.display(description="Cliques",ordering="total")
 def total_cliques(self,obj): return obj.total if hasattr(obj,"total") else obj.cliques.count()
 @admin.display(description="Foto")
 def imagem_preview(self,obj):
  url=obj.imagem.url if obj.imagem else obj.imagem_externa
  return format_html('<img src="{}" alt="Prévia" style="max-width:180px;max-height:180px;border-radius:10px">',url) if url else "Sem imagem"
 @admin.display(description="Link")
 def situacao_link(self,obj):
  try: obj.full_clean();return "Válido"
  except ValidationError: return "Revisar"
 @admin.action(description="Aprovar e publicar ofertas selecionadas")
 def aprovar(self,request,queryset):
  ok=0
  for oferta in queryset.select_related("parceiro","categoria"):
   if not oferta.parceiro.ativo or not oferta.categoria.ativa:
    self.message_user(request,f"Parceiro/categoria inativo: {oferta.nome}",level=messages.WARNING)
    continue
   oferta.status_revisao=ProdutoAfiliado.Revisao.APROVADO
   oferta.ativo=True
   try: oferta.full_clean();oferta.save(update_fields=["status_revisao","ativo"]);ok+=1
   except ValidationError as exc: self.message_user(request,f"{oferta.nome}: {exc}",level=messages.ERROR)
  self.message_user(request,f"{ok} oferta(s) aprovada(s).")
 @admin.action(description="Rejeitar e despublicar ofertas")
 def rejeitar(self,request,queryset): self.message_user(request,f'{queryset.update(status_revisao=ProdutoAfiliado.Revisao.REJEITADO,ativo=False)} oferta(s) rejeitada(s).')
 @admin.action(description="Despublicar ofertas")
 def despublicar(self,request,queryset): self.message_user(request,f'{queryset.update(ativo=False)} oferta(s) despublicada(s).')
 @admin.action(description="Destacar ofertas")
 def destacar(self,request,queryset): self.message_user(request,f'{queryset.update(destaque=True)} oferta(s) destacada(s).')
 @admin.action(description="Retirar destaque")
 def retirar_destaque(self,request,queryset): self.message_user(request,f'{queryset.update(destaque=False)} destaque(s) removido(s).')

@admin.register(CliqueAfiliado)
class CliqueAfiliadoAdmin(admin.ModelAdmin):
 list_display=("produto","criado_em")
 list_filter=("criado_em",)
 search_fields=("produto__nome",)
 readonly_fields=("produto","criado_em")
 def has_add_permission(self,request): return False
 def has_change_permission(self,request,obj=None): return False
 def has_delete_permission(self,request,obj=None): return False
