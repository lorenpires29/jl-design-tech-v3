from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
User=get_user_model()
class ContasTests(TestCase):
 def test_cadastro_e_perfil(self):
  response=self.client.post(reverse("cadastro"),{"username":"ana","first_name":"Ana","email":"ana@example.com","password1":"SenhaMuitoForte2026!","password2":"SenhaMuitoForte2026!"})
  self.assertEqual(response.status_code,302)
  self.assertTrue(User.objects.filter(username="ana").exists())
  self.assertEqual(self.client.get(reverse("perfil")).status_code,200)
 def test_perfil_exige_login(self):
  self.assertEqual(self.client.get(reverse("perfil")).status_code,302)
 def test_logout_somente_post(self):
  User.objects.create_user("ana",password="SenhaMuitoForte2026!")
  self.client.login(username="ana",password="SenhaMuitoForte2026!")
  self.assertEqual(self.client.get(reverse("logout")).status_code,405)
  self.assertEqual(self.client.post(reverse("logout")).status_code,302)
 def test_dashboard_bloqueado(self):
  self.assertEqual(self.client.get(reverse("dashboard")).status_code,302)
  User.objects.create_user("ana",password="SenhaMuitoForte2026!")
  self.client.login(username="ana",password="SenhaMuitoForte2026!")
  self.assertEqual(self.client.get(reverse("dashboard")).status_code,403)
