from django.test import TestCase
from django.core.exceptions import ValidationError
from catalogo.models import Categoria,Produto
from .models import ConexaoShopee,VinculoAnuncio
class IntegracaoTests(TestCase):
 def test_nao_simular_autorizacao(self):
  c=ConexaoShopee.objects.create(nome="Teste")
  self.assertEqual(c.status,"nao_configurada")
  cat=Categoria.objects.create(nome="Teste",slug="teste")
  p=Produto.objects.create(categoria=cat,nome="Peça",slug="peca",descricao="Peça")
  v=VinculoAnuncio(conexao=c,produto=p,anuncio_externo_id="ABC",ativo=True)
  with self.assertRaises(ValidationError): v.full_clean()
