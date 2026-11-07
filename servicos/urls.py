from django.urls import path
from . import views
urlpatterns=[path("servicos/",views.lista,name="servicos"),path("servicos/<slug:slug>/",views.detalhe,name="servico_detalhe"),path("orcamento/solicitar/",views.solicitar,name="solicitar_orcamento"),path("orcamento/recebido/",views.sucesso,name="orcamento_sucesso")]
