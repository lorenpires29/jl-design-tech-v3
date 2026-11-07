from django.urls import path
from . import views
urlpatterns=[path("produtos/",views.lista,name="produtos"),path("produtos/<slug:slug>/",views.detalhe,name="produto_detalhe"),path("comprar/shopee/<int:pk>/",views.comprar,name="comprar_shopee")]
