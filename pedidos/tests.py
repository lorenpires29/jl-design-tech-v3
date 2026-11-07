from decimal import Decimal
from django.test import TestCase
from django.db import IntegrityError
from integracoes.models import ConexaoShopee
from .models import PedidoExterno,HistoricoStatusPedido,ItemPedido
from .services import conciliar_pedido
class PedidoTests(TestCase):
 def setUp(self):
  self.conexao=ConexaoShopee.objects.create(nome="Loja de teste")
  self.dados=dict(conexao=self.conexao,identificador_externo="PED-001",status_externo="novo",itens=[dict(descricao="Peça 3D",quantidade=2,preco_unitario="12.50")],total=Decimal("25.00"))
 def test_importacao_idempotente(self):
  p,criado=conciliar_pedido(**self.dados)
  self.assertTrue(criado)
  p2,criado=conciliar_pedido(**self.dados)
  self.assertFalse(criado)
  self.assertEqual(p.pk,p2.pk)
  self.assertEqual(PedidoExterno.objects.count(),1)
  self.assertEqual(ItemPedido.objects.count(),1)
  self.assertEqual(HistoricoStatusPedido.objects.count(),1)
 def test_historico_mudanca(self):
  conciliar_pedido(**self.dados)
  conciliar_pedido(**{**self.dados,"status_externo":"enviado"})
  self.assertEqual(HistoricoStatusPedido.objects.count(),2)
 def test_sem_dados_comprador(self):
  self.assertFalse(any("cpf" in f.name or "email" in f.name or "telefone" in f.name for f in PedidoExterno._meta.fields))
