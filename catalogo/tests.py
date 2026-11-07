from django.test import TestCase
from django.urls import reverse
from django.core.exceptions import ValidationError
from .models import Categoria,Produto,AnuncioShopee
class CatalogoTests(TestCase):
 def setUp(self): self.cat=Categoria.objects.create(nome="Presentes",slug="presentes")
 def test_listagem(self):
  for i in range(15): Produto.objects.create(categoria=self.cat,nome=f"Peça {i}",slug=f"peca-{i}",descricao="Teste")
  r=self.client.get(reverse("produtos"))
  self.assertEqual(len(r.context["produtos"]),12)
 def test_inativo(self):
  p=Produto.objects.create(categoria=self.cat,nome="Oculto",slug="oculto",descricao="Teste",ativo=False)
  self.assertEqual(self.client.get(reverse("produto_detalhe",args=[p.slug])).status_code,404)
 def test_link_shopee(self):
  p=Produto.objects.create(categoria=self.cat,nome="Caneca",slug="caneca",descricao="Teste")
  a=AnuncioShopee.objects.create(produto=p,url="https://shopee.com.br/produto")
  self.assertEqual(self.client.get(reverse("comprar_shopee",args=[a.pk])).status_code,302)
  with self.assertRaises(ValidationError): AnuncioShopee.objects.create(produto=p,url="https://example.com/falso")
