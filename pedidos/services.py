from decimal import Decimal
from django.db import transaction
from .models import PedidoExterno,ItemPedido,HistoricoStatusPedido

@transaction.atomic
def conciliar_pedido(*,conexao,identificador_externo,status_externo,itens,origem="arquivo",total=None,moeda="BRL",data_pedido=None):
 """Importação explícita autorizada: reprocessar não duplica pedido nem histórico sem mudança de status."""
 if origem not in ("arquivo","api"): raise ValueError("Origem inválida")
 if not identificador_externo or not status_externo: raise ValueError("Identificador e status são obrigatórios")
 if len(identificador_externo)>120 or len(status_externo)>100: raise ValueError("Campos acima do limite")
 if moeda!="BRL": raise ValueError("Somente BRL nesta versão")
 itens=list(itens)
 if not itens: raise ValueError("Pedido deve conter itens")
 for item in itens:
  if int(item["quantidade"])<=0 or Decimal(str(item["preco_unitario"]))<0: raise ValueError("Item inválido")
 pedido,criado=PedidoExterno.objects.select_for_update().get_or_create(conexao=conexao,identificador_externo=identificador_externo,defaults={"status_externo":status_externo,"total":total,"moeda":moeda,"data_pedido":data_pedido})
 anterior="" if criado else pedido.status_externo
 if criado or anterior!=status_externo:
  HistoricoStatusPedido.objects.create(pedido=pedido,status_anterior=anterior,status_novo=status_externo,origem=origem)
 if not criado:
  pedido.status_externo=status_externo
  pedido.total=total
  pedido.moeda=moeda
  pedido.data_pedido=data_pedido
  pedido.save(update_fields=["status_externo","total","moeda","data_pedido","sincronizado_em"])
 pedido.itens.all().delete()
 ItemPedido.objects.bulk_create([ItemPedido(pedido=pedido,identificador_produto=str(x.get("identificador_produto",""))[:120],descricao=str(x["descricao"])[:240],quantidade=int(x["quantidade"]),preco_unitario=Decimal(str(x["preco_unitario"]))) for x in itens])
 return pedido,criado
