from django.core.exceptions import ValidationError
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import Http404
from django.shortcuts import get_object_or_404,render,redirect
from .models import Produto,Categoria,AnuncioShopee,CliqueAnuncio
def lista(request):
 produtos=Produto.objects.filter(ativo=True,categoria__ativa=True).select_related("categoria")
 q=request.GET.get("q","").strip()[:120]
 categoria=request.GET.get("categoria","").strip()
 ordem=request.GET.get("ordem","-criado_em")
 if q: produtos=produtos.filter(Q(nome__icontains=q)|Q(descricao__icontains=q))
 if categoria: produtos=produtos.filter(categoria__slug=categoria)
 if ordem not in ("-criado_em","nome","preco_referencia","-preco_referencia"): ordem="-criado_em"
 return render(request,"catalogo/lista.html",{"produtos":Paginator(produtos.order_by(ordem,"id"),12).get_page(request.GET.get("page")),"categorias":Categoria.objects.filter(ativa=True),"q":q,"categoria_atual":categoria,"ordem":ordem})
def detalhe(request,slug):
 p=get_object_or_404(Produto,slug=slug,ativo=True,categoria__ativa=True)
 return render(request,"catalogo/detalhe.html",{"produto":p,"anuncios":p.anuncios.filter(ativo=True)})
def comprar(request,pk):
 a=get_object_or_404(AnuncioShopee,pk=pk,ativo=True,produto__ativo=True,produto__categoria__ativa=True)
 try: a.full_clean()
 except ValidationError as e: raise Http404("Anúncio indisponível") from e
 CliqueAnuncio.objects.create(anuncio=a)
 return redirect(a.url)
