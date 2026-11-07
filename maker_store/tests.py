from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse
from .models import Parceiro,CategoriaAfiliado,ProdutoAfiliado,CliqueAfiliado
class MakerStoreTests(TestCase):
 def setUp(self):
  self.parceiro=Parceiro.objects.get(slug="collshp")
  self.categoria=CategoriaAfiliado.objects.get(slug="filamentos")
 def produto(self,**kwargs):
  d={"parceiro":self.parceiro,"categoria":self.categoria,"nome":"Filamento PLA","slug":"filamento-pla","url_destino":"https://collshp.com/lorenpires993?view=storefront","status_revisao":"aprovado","ativo":True}
  d.update(kwargs)
  return ProdutoAfiliado.objects.create(**d)
 def test_vitrine_e_filtros(self):
  self.produto()
  self.assertContains(self.client.get(reverse("maker_store")),"Filamento PLA")
  self.assertContains(self.client.get(reverse("maker_store"),{"categoria":"filamentos","parceiro":"collshp","q":"PLA"}),"Filamento PLA")
  self.assertNotContains(self.client.get(reverse("maker_store"),{"q":"ABS"}),"Filamento PLA</")
 def test_revisao_obrigatoria(self):
  with self.assertRaises(ValidationError): self.produto(status_revisao="pendente")
 def test_link_invalido(self):
  with self.assertRaises(ValidationError): self.produto(url_destino="https://example.org/redirect")
 def test_clique_e_inatividade(self):
  p=self.produto()
  r=self.client.get(reverse("maker_visitar",args=[p.pk]))
  self.assertEqual(r.status_code,302)
  self.assertEqual(CliqueAfiliado.objects.filter(produto=p).count(),1)
  p.ativo=False
  p.save()
  self.assertEqual(self.client.get(reverse("maker_visitar",args=[p.pk])).status_code,404)
  self.assertEqual(CliqueAfiliado.objects.count(),1)
 def test_sem_aprovacao_nao_publica(self):
  self.produto(ativo=False,status_revisao="pendente")
  self.assertNotContains(self.client.get(reverse("maker_store")),"filamento-pla/")
