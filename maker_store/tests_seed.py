from django.test import TestCase
from django.urls import reverse
from .models import ProdutoAfiliado
class VitrineSeedTests(TestCase):
 def test_itens_iniciais_visiveis(self):
  # Data migration runs before Django TestCase creates the test database.
  self.assertGreaterEqual(ProdutoAfiliado.objects.filter(parceiro__slug="collshp").count(),6)
  response=self.client.get(reverse("maker_store"))
  self.assertContains(response,"Filamento PLA Silk SOL3D")
  self.assertContains(response,"Kit de Ferramentas")
