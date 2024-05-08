from django.shortcuts import render, get_object_or_404, redirect
from .models import Fotografia
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
#@login_required
def index(request):
    if not request.user.is_authenticated:
        messages.error(request, "você precisa está logado para acessar a home do nosso site!")
        return redirect('usuarios:login')
    
    all_fotografias = Fotografia.objects.order_by("-data").filter(publicada=True)
    tipos_categoria = Fotografia._meta.get_field('categoria').choices
    return render(request, 'galeria/index.html', {
        "fotos": all_fotografias,
        "categorias": tipos_categoria,
    })

#@login_required
def detail(request, pk):
    if not request.user.is_authenticated:
        messages.error(request, "você precisa está logado para acessar o nosso site!")
        return redirect('usuarios:login')

    fotografia = get_object_or_404(Fotografia, pk=pk)
    return render(request, 'galeria/imagem.html', {
        "fotografia": fotografia,
    })

#@login_required
def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, "você precisa está logado para acessar o nosso site!")
        return redirect('usuarios:login')

    all_fotografias = Fotografia.objects.order_by("-data").filter(publicada=True)
    if "buscar" in request.GET:
        palavra_search = request.GET['buscar']
        if palavra_search:
            fotografias_buscada = all_fotografias.filter(nome__icontains=palavra_search)
        else:
            fotografias_buscada = ""

    return render(request, 'galeria/buscar.html', {
        "fotos": fotografias_buscada,
        "palavra_buscada": palavra_search,
    })