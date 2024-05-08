from django.shortcuts import render, redirect
from .forms import LoginForm, CadastroForm
from django.contrib.auth.models import User
from django.contrib import auth, messages


# Create your views here.
def login(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            nome = login_form['nome'].value()
            senha = login_form['senha'].value()

            usuario = auth.authenticate(
                request,
                username=nome,
                password=senha,
            )
            if usuario is not None:
                auth.login(request, usuario)
                return redirect('galeria:index')
            else:
                messages.error(request, "Usuario ou senha incorretos!")
                return redirect('usuarios:login')
        else:
            messages.error(request, "Não foi possivel realizar o login!")
            return redirect('usuarios:login')
    else:
        login_form = LoginForm()
    return render(request, 'usuarios/login.html', {
        "login_form": login_form,
    })

def cadastro(request):
    if request.method == "POST":
        cadastro_form = CadastroForm(request.POST)

        if cadastro_form.is_valid():
            nome = cadastro_form['nome'].value()
            email = cadastro_form['email'].value()
            senha = cadastro_form['senha'].value()

            if User.objects.filter(username=nome).exists():
                messages.error(request, "username já existente!")
                return redirect('usuarios:cadastro')
            
            user = User.objects.create_user(username=nome,email=email,password=senha)
            user.save()
            messages.success(request, "Usuario criado com sucesso!")
            return redirect('usuarios:login')

    else:
        cadastro_form = CadastroForm()
    
    return render(request, 'usuarios/cadastro.html', {
        "cadastro_form": cadastro_form,
    })

def logout(request):
    auth.logout(request)
    messages.success(request, "logout efetuado com sucesso!")
    return redirect('usuarios:login')