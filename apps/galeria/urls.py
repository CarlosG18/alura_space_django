from django.urls import path
from . import views

app_name='galeria'

urlpatterns = [
    path('', views.index, name="index"),
    path('imagem/<int:pk>/', views.detail, name="detail"),
    path('buscar', views.buscar, name="buscar"),
]