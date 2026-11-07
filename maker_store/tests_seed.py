from django.test import TestCase
from django.urls import reverse
from .models import ProdutoAfiliado
class VitrineSeedTests(TestCase):
 def test_itens_iniciais_visiveis(self):
  self.assertGreaterEqual(ProdutoAfiliado.objects.filter(parceiro__slug="collshp").count(),6)
  response=self.client.get(reverse("maker_store"))
  self.assertContains(response,"Filamento PLA Silk SOL3D")
  self.assertContains(response,"Kit de Ferramentas")
 def test_fotos_kits(self):
  for slug in ("kit-ferramentas-impressora-3d-9-pecas","kit-ferramentas-impressora-3d-ate-60-pecas"):
   p=ProdutoAfiliado.objects.get(slug=slug)
   self.assertTrue(p.imagem_externa.startswith("https://down-br.img.susercontent.com/"))
   self.assertContains(self.client.get(reverse("maker_detalhe",args=[slug])),p.imagem_externa)
