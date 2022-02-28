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

        path('libros/', views.listarLibros, name='libros'),
    path('libros/new', views.create_libro, name='new_libro'),
    path('libros/<id>/', views.detail_viewBook, name='libro_detail'),
    path('libros/update/<id>/', views.update_libro, name='libro_update'),
    path('libros/delete/<id>/', views.delete_viewBook, name='libro_delete'),

    
]