from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('autores/', views.listarAutores, name='autores'),
    path('autores/new', views.create_autor, name='new_autor'),
    path('autores/<id>/', views.detail_view, name='autor_detail'),
    path('autores/update/<id>/', views.update_autor, name='autor_update'),
    path('autores/delete/<id>/', views.delete_view, name='autor_delete'),
]