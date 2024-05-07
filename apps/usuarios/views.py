from django.shortcuts import render
from .forms import LoginForm, CadastroForm

# Create your views here.
def login(request):
    if request.method == "POST":
        pass
    else:
        login_form = LoginForm()
    return render(request, 'usuarios/login.html', {
        "login_form": login_form,
    })

def cadastro(request):
    if request.method == "POST":
        pass
    else:
        cadastro_form = CadastroForm()
    
    return render(request, 'usuarios/cadastro.html', {
        "cadastro_form": cadastro_form,
    })