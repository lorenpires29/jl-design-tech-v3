from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.views.decorators.http import require_http_methods
from .forms import CadastroForm,PerfilForm
@require_http_methods(["GET","POST"])
def cadastro(request):
 if request.user.is_authenticated: return redirect("perfil")
 form=CadastroForm(request.POST or None)
 if request.method=="POST" and form.is_valid():
  user=form.save()
  login(request,user)
  messages.success(request,"Conta criada com sucesso.")
  return redirect("perfil")
 return render(request,"contas/form.html",{"form":form,"titulo":"Criar conta","botao":"Cadastrar"})
@login_required
@require_http_methods(["GET","POST"])
def perfil(request):
 form=PerfilForm(request.POST or None,instance=request.user)
 if request.method=="POST" and form.is_valid():
  form.save()
  messages.success(request,"Perfil atualizado.")
  return redirect("perfil")
 return render(request,"contas/form.html",{"form":form,"titulo":"Meu perfil","botao":"Salvar alterações"})
