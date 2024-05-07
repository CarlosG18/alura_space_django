from django.shortcuts import render, get_object_or_404
from .models import Fotografia

# Create your views here.
def index(request):
    all_fotografias = Fotografia.objects.order_by("-data").filter(publicada=True)
    tipos_categoria = Fotografia._meta.get_field('categoria').choices
    return render(request, 'galeria/index.html', {
        "fotos": all_fotografias,
        "categorias": tipos_categoria,
    })

def detail(request, pk):
    fotografia = get_object_or_404(Fotografia, pk=pk)
    return render(request, 'galeria/imagem.html', {
        "fotografia": fotografia,
    })

def buscar(request):
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