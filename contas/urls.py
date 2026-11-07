from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
urlpatterns=[
 path("conta/cadastro/",views.cadastro,name="cadastro"),
 path("conta/perfil/",views.perfil,name="perfil"),
 path("conta/entrar/",auth_views.LoginView.as_view(template_name="contas/login.html"),name="login"),
 path("conta/sair/",auth_views.LogoutView.as_view(),name="logout"),
 path("conta/senha/recuperar/",auth_views.PasswordResetView.as_view(template_name="contas/form.html",email_template_name="contas/reset_email.txt",subject_template_name="contas/reset_assunto.txt",success_url="/conta/senha/enviada/",extra_context={"titulo":"Recuperar senha","botao":"Enviar link"}),name="password_reset"),
 path("conta/senha/enviada/",auth_views.PasswordResetDoneView.as_view(template_name="contas/reset_enviado.html"),name="password_reset_done"),
 path("conta/senha/redefinir/<uidb64>/<token>/",auth_views.PasswordResetConfirmView.as_view(template_name="contas/form.html",success_url="/conta/senha/concluida/",extra_context={"titulo":"Definir nova senha","botao":"Salvar nova senha"}),name="password_reset_confirm"),
 path("conta/senha/concluida/",auth_views.PasswordResetCompleteView.as_view(template_name="contas/reset_concluido.html"),name="password_reset_complete"),
]