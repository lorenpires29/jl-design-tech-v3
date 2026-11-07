from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
class DashboardTests(TestCase):
 def setUp(self):
  self.staff=get_user_model().objects.create_user("staff",password="SenhaMuitoForte2026!",is_staff=True)
 def test_periodos_e_acesso(self):
  self.client.force_login(self.staff)
  for periodo in ("7","30","90","invalido"):
   response=self.client.get(reverse("dashboard"),{"periodo":periodo})
   self.assertEqual(response.status_code,200)
  self.assertContains(response,"Não configurada")

 def test_menu_respeita_permissoes(self):
  self.client.force_login(self.staff)
  response=self.client.get(reverse("dashboard"))
  self.assertNotContains(response,"admin:catalogo_produto_changelist")
  self.assertNotContains(response,'href="/admin/catalogo/produto/"')
 def test_status_conexao_nao_e_fixo(self):
  from integracoes.models import ConexaoShopee
  ConexaoShopee.objects.create(nome="Loja pendente",status="pendente")
  self.client.force_login(self.staff)
  self.assertContains(self.client.get(reverse("dashboard")),"1 conexão(ões) cadastrada(s)")
