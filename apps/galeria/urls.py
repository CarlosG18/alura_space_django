from django.urls import path
from . import views

app_name='galeria'

urlpatterns = [
    path('', views.index, name="index"),
    path('imagem/<int:pk>/', views.detail, name="detail"),
    path('buscar', views.buscar, name="buscar"),
    path('add/', views.add_imagem, name="add_foto"),
    path('editar/<int:id>', views.editar_imagem, name="editar_foto"),
    path('deletar/<int:id>', views.deletar_imagem, name="deletar_foto"),
    path('filtro/<str:cat>', views.filtro_cat, name="filtro_cat"),
]