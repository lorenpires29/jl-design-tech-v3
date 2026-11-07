from django.core.exceptions import ValidationError
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import Http404
from django.shortcuts import get_object_or_404,redirect,render
from django.views.decorators.http import require_GET
from .models import Parceiro,CategoriaAfiliado,ProdutoAfiliado,CliqueAfiliado

def publicados():
 return ProdutoAfiliado.objects.filter(ativo=True,status_revisao=ProdutoAfiliado.Revisao.APROVADO,parceiro__ativo=True,categoria__ativa=True)

@require_GET
def vitrine(request):
 itens=publicados().select_related("parceiro","categoria")
 q=request.GET.get("q","").strip()[:120]
 categoria=request.GET.get("categoria","").strip()
 parceiro=request.GET.get("parceiro","").strip()
 if q: itens=itens.filter(Q(nome__icontains=q)|Q(descricao__icontains=q))
 if categoria: itens=itens.filter(categoria__slug=categoria)
 if parceiro: itens=itens.filter(parceiro__slug=parceiro)
 return render(request,"maker_store/vitrine.html",{"produtos":Paginator(itens,12).get_page(request.GET.get("page")),"categorias":CategoriaAfiliado.objects.filter(ativa=True),"parceiros":Parceiro.objects.filter(ativo=True),"q":q,"categoria_atual":categoria,"parceiro_atual":parceiro})

@require_GET
def detalhe(request,slug):
 return render(request,"maker_store/detalhe.html",{"produto":get_object_or_404(publicados(),slug=slug)})

@require_GET
def visitar(request,pk):
 produto=get_object_or_404(publicados(),pk=pk)
 try: produto.full_clean()
 except ValidationError as exc: raise Http404("Oferta indisponível") from exc
 CliqueAfiliado.objects.create(produto=produto)
 return redirect(produto.url_destino)
