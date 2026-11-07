from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Parceiro,CategoriaAfiliado,ProdutoAfiliado
class AfiliadosAdminTests(TestCase):
 def setUp(self):
  self.user=get_user_model().objects.create_superuser("gestor","gestor@example.com","SenhaMuitoForte2026!")
  self.client.force_login(self.user)
  self.parceiro=Parceiro.objects.get(slug="collshp")
  self.categoria=CategoriaAfiliado.objects.get(slug="filamentos")
  self.oferta=ProdutoAfiliado.objects.get(slug="filamento-pla-silk-sol3d-1kg")
 def test_telas_admin(self):
  for name in ("maker_store_produtoafiliado_changelist","maker_store_parceiro_changelist","maker_store_categoriaafiliado_changelist","maker_store_cliqueafiliado_changelist"):
   self.assertEqual(self.client.get(reverse("admin:"+name)).status_code,200)
 def test_rejeitar_e_aprovar(self):
  url=reverse("admin:maker_store_produtoafiliado_changelist")
  self.client.post(url,{"action":"rejeitar","_selected_action":[self.oferta.pk],"index":"0"})
  self.oferta.refresh_from_db()
  self.assertFalse(self.oferta.ativo)
  self.assertEqual(self.oferta.status_revisao,"rejeitado")
  self.client.post(url,{"action":"aprovar","_selected_action":[self.oferta.pk],"index":"0"})
  self.oferta.refresh_from_db()
  self.assertTrue(self.oferta.ativo)
  self.assertEqual(self.oferta.status_revisao,"aprovado")
 def test_link_invalido_nao_publica(self):
  ProdutoAfiliado.objects.filter(pk=self.oferta.pk).update(url_destino="https://example.org/")
  url=reverse("admin:maker_store_produtoafiliado_changelist")
  self.client.post(url,{"action":"aprovar","_selected_action":[self.oferta.pk],"index":"0"})
  self.oferta.refresh_from_db()
  self.assertEqual(self.oferta.url_destino,"https://example.org/")
