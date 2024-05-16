from django.shortcuts import render, get_object_or_404, redirect
from .models import Fotografia
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import FotografiaForm

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
    tipos_categoria = Fotografia._meta.get_field('categoria').choices
    if "buscar" in request.GET:
        palavra_search = request.GET['buscar']
        if palavra_search:
            fotografias_buscada = all_fotografias.filter(nome__icontains=palavra_search)
        else:
            fotografias_buscada = ""

    return render(request, 'galeria/index.html', {
        "fotos": fotografias_buscada,
        "palavra_buscada": palavra_search,
        "buscar": True,
        "categorias": tipos_categoria,
    })

def add_imagem(request):
    if not request.user.is_authenticated:
        messages.error(request, "você precisa está logado para acessar o nosso site!")
        return redirect('usuarios:login')

    if request.method == "POST":
        form = FotografiaForm(request.POST,request.FILES)

        if form.is_valid():
            imagem = form.save(commit=False)
            imagem.usuario = request.user
            imagem.save()
            messages.success(request,"foto adicionada com sucesso!")
            return redirect('galeria:index')

    else:
        form = FotografiaForm()
    return render(request, 'galeria/add_foto.html', {
        "form": form,
    })

def deletar_imagem(request, id):
    imagem = Fotografia.objects.get(id=id)
    imagem.delete()
    messages.success(request, "fotografia deletada com sucesso!")
    return redirect('galeria:index')

def editar_imagem(request, id):
    imagem = Fotografia.objects.get(id=id)
    
    if not request.user.is_authenticated:
        messages.error(request, "você precisa está logado para acessar o nosso site!")
        return redirect('usuarios:login')

    if request.method == "POST":
        form = FotografiaForm(request.POST,request.FILES, instance=imagem)

        if form.is_valid():
            form.save()
            messages.success(request,"foto editada com sucesso!")
            return redirect('galeria:index')

    else:
        form = FotografiaForm(instance=imagem)
    return render(request, 'galeria/editar_foto.html', {
        "form": form,
        "img_id": id, 
    })

def filtro_cat(request, cat):
    fotografias = Fotografia.objects.filter(publicada=True, categoria=cat)
    tipos_categoria = Fotografia._meta.get_field('categoria').choices

    return render(request, 'galeria/index.html', {
        "fotos": fotografias,
        "categorias": tipos_categoria,
    })