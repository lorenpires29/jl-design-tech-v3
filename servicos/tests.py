from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse
from .models import Servico,SolicitacaoOrcamento
class ServicosTests(TestCase):
 def setUp(self):
  self.servico=Servico.objects.create(nome="Impressão 3D",slug="impressao-3d",resumo="Protótipos",descricao="Produção de peças")
 def dados(self):
  return {"nome":"Maria","email":"maria@example.com","servico":self.servico.pk,"descricao":"Preciso de uma peça personalizada para meu projeto.","quantidade":2}
 def test_listar_pesquisar_e_detalhar(self):
  self.assertContains(self.client.get(reverse("servicos")),"Impressão 3D")
  self.assertContains(self.client.get(reverse("servicos"),{"q":"Protótipos"}),"Impressão 3D")
  self.assertEqual(self.client.get(reverse("servico_detalhe",args=["impressao-3d"])).status_code,200)
  self.servico.ativo=False
  self.servico.save()
  self.assertEqual(self.client.get(reverse("servico_detalhe",args=["impressao-3d"])).status_code,404)
 def test_criar_e_validar(self):
  url=reverse("solicitar_orcamento")
  self.assertEqual(self.client.post(url,{**self.dados(),"descricao":"curto"}).status_code,200)
  self.assertEqual(SolicitacaoOrcamento.objects.count(),0)
  self.assertEqual(self.client.post(url,self.dados()).status_code,302)
  self.assertEqual(SolicitacaoOrcamento.objects.count(),1)
 def test_arquivo_invalido(self):
  arquivo=SimpleUploadedFile("referencia.pdf",b"arquivo falso",content_type="application/pdf")
  self.client.post(reverse("solicitar_orcamento"),{**self.dados(),"referencia":arquivo})
  self.assertEqual(SolicitacaoOrcamento.objects.count(),0)
