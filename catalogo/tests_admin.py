from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Categoria,Produto
class CatalogoAdminTests(TestCase):
 def setUp(self):
  self.user=get_user_model().objects.create_superuser("gestor","gestor@example.com","SenhaMuitoForte2026!")
  self.client.force_login(self.user)
  self.categoria=Categoria.objects.create(nome="Eletrônicos",slug="eletronicos")
  self.produto=Produto.objects.create(nome="Peça 3D",slug="peca-3d",categoria=self.categoria,descricao="Peça personalizada")
 def test_telas_administrativas(self):
  for name in ("catalogo_produto_changelist","catalogo_categoria_changelist","catalogo_anuncioshopee_changelist"):
   self.assertEqual(self.client.get(reverse("admin:"+name)).status_code,200)
 def test_publicacao_e_destaque(self):
  url=reverse("admin:catalogo_produto_changelist")
  self.client.post(url,{"action":"despublicar","_selected_action":[self.produto.pk],"index":"0"})
  self.produto.refresh_from_db()
  self.assertFalse(self.produto.ativo)
  self.client.post(url,{"action":"publicar","_selected_action":[self.produto.pk],"index":"0"})
  self.produto.refresh_from_db()
  self.assertTrue(self.produto.ativo)
 def test_categoria_inativa_nao_publica(self):
  self.produto.ativo=False;self.produto.save()
  self.categoria.ativa=False;self.categoria.save()
  self.client.post(reverse("admin:catalogo_produto_changelist"),{"action":"publicar","_selected_action":[self.produto.pk],"index":"0"})
  self.produto.refresh_from_db()
  self.assertFalse(self.produto.ativo)
