from django.contrib import admin
from .models import PedidoExterno,ItemPedido,HistoricoStatusPedido
class ItemInline(admin.TabularInline):
 model=ItemPedido
 extra=0
 readonly_fields=("identificador_produto","descricao","quantidade","preco_unitario")
 def has_add_permission(self,request,obj=None): return False
 def has_delete_permission(self,request,obj=None): return False
class HistoricoInline(admin.TabularInline):
 model=HistoricoStatusPedido
 extra=0
 readonly_fields=("status_anterior","status_novo","origem","registrado_em")
 def has_add_permission(self,request,obj=None): return False
 def has_delete_permission(self,request,obj=None): return False
@admin.register(PedidoExterno)
class PedidoExternoAdmin(admin.ModelAdmin):
 list_display=("identificador_externo","conexao","status_externo","total","moeda","divergente","sincronizado_em")
 list_filter=("conexao","status_externo","divergente","sincronizado_em")
 search_fields=("identificador_externo",)
 readonly_fields=("conexao","identificador_externo","status_externo","total","moeda","data_pedido","sincronizado_em","divergente")
 inlines=(ItemInline,HistoricoInline)
 def has_add_permission(self,request): return False
 def has_change_permission(self,request,obj=None): return False
 def has_delete_permission(self,request,obj=None): return False
