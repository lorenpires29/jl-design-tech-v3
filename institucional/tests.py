from django.test import TestCase
from django.urls import reverse
from .models import MensagemContato
class InstitucionalTests(TestCase):
 def test_home(self): self.assertContains(self.client.get(reverse("home")),"Nossa")
 def test_sobre(self): self.assertContains(self.client.get(reverse("sobre")),"Projetando ideias")
 def test_contato(self):
  url=reverse("contato")
  self.client.post(url,{"nome":"Ana","email":"ana@example.com","mensagem":"curta"})
  self.assertEqual(MensagemContato.objects.count(),0)
  r=self.client.post(url,{"nome":"Ana","email":"ana@example.com","mensagem":"Preciso de uma peça personalizada."})
  self.assertEqual(r.status_code,302)
  self.assertEqual(MensagemContato.objects.count(),1)

 def test_cta_orcamento_aponta_para_formulario(self):
  response=self.client.get(reverse("home"))
  self.assertContains(response,'href="'+reverse("solicitar_orcamento")+'">Solicitar orçamento')
