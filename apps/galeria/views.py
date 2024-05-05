from django.shortcuts import render, get_object_or_404
from .models import Fotografia

# Create your views here.
def index(request):
    all_fotografias = Fotografia.objects.order_by("-data").filter(publicada=True)
    tipos_categoria = Fotografia._meta.get_field('categoria').choices
    return render(request, 'index.html', {
        "fotos": all_fotografias,
        "categorias": tipos_categoria,
    })

def detail(request, pk):
    fotografia = get_object_or_404(Fotografia, pk=pk)
    return render(request, 'imagem.html', {
        "fotografia": fotografia,
    })