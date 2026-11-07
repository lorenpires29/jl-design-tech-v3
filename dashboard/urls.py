from django.urls import path
from .views import inicio
urlpatterns=[path("painel/",inicio,name="dashboard")]
