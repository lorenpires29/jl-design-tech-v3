from django.contrib import messages
from django.shortcuts import render,redirect
from django.views.decorators.http import require_http_methods
from catalogo.models import Produto
from .forms import ContatoForm
def home(request): return render(request,"institucional/home.html",{"destaques":Produto.objects.filter(ativo=True,destaque=True)[:5]})
def sobre(request): return render(request,"institucional/sobre.html")
@require_http_methods(["GET","POST"])
def contato(request):
 form=ContatoForm(request.POST or None)
 if request.method=="POST" and form.is_valid():
  form.save()
  messages.success(request,"Mensagem recebida com sucesso!")
  return redirect("contato")
 return render(request,"institucional/contato.html",{"form":form})
