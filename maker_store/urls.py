from django.urls import path
from . import views
urlpatterns=[path("maker-store/",views.vitrine,name="maker_store"),path("maker-store/<slug:slug>/",views.detalhe,name="maker_detalhe"),path("maker-store/visitar/<int:pk>/",views.visitar,name="maker_visitar")]
