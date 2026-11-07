from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404,render,redirect
from django.views.decorators.http import require_http_methods
from .models import Servico
from .forms import SolicitacaoForm

def lista(request):
 q=request.GET.get("q","").strip()[:120]
 items=Servico.objects.filter(ativo=True)
 if q: items=items.filter(Q(nome__icontains=q)|Q(resumo__icontains=q)|Q(descricao__icontains=q))
 return render(request,"servicos/lista.html",{"servicos":Paginator(items,12).get_page(request.GET.get("page")),"q":q})

def detalhe(request,slug):
 return render(request,"servicos/detalhe.html",{"servico":get_object_or_404(Servico,slug=slug,ativo=True)})

@require_http_methods(["GET","POST"])
def solicitar(request):
 form=SolicitacaoForm(request.POST or None,request.FILES or None,initial={"servico":request.GET.get("servico")} if request.method=="GET" else None)
 if request.method=="POST" and form.is_valid():
  form.save()
  messages.success(request,"Solicitação recebida! Nossa equipe entrará em contato.")
  return redirect("orcamento_sucesso")
 return render(request,"servicos/solicitar.html",{"form":form})

def sucesso(request):
 return render(request,"servicos/sucesso.html")
