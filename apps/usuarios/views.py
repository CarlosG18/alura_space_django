from django.shortcuts import render, redirect
from .forms import LoginForm, CadastroForm
from django.contrib.auth.models import User
from django.contrib import auth, messages


# Create your views here.
def login(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            nome = login_form.cleaned_data['nome']
            senha = login_form.cleaned_data['senha']

            usuario = auth.authenticate(
                request,
                username=nome,
                password=senha,
            )
            if usuario is not None:
                auth.login(request, usuario)
                messages.success(request, "Login efetuado com sucesso!")
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
        #data = {
            #"nome": request.POST['nome'],
            #"email": request.POST['email'],
            #"senha": request.POST['senha'],
            #"senha_confirmar": request.POST['senha_confirmar'],
        #}
    
        #cadastro_form = CadastroForm(data=data)
        cadastro_form = CadastroForm(request.POST)

        if cadastro_form.is_valid():
            if cadastro_form.cleaned_data['senha'] != cadastro_form.cleaned_data['senha_confirmar']:
                messages.error(request, "senhas são incompativeis!")
                return redirect('usuarios:cadastro')
        
            nome = cadastro_form.cleaned_data['nome']
            email = cadastro_form.cleaned_data['email']
            senha = cadastro_form.cleaned_data['senha']

            if User.objects.filter(username=nome).exists():
                messages.error(request, "username já existente!")
                return redirect('usuarios:cadastro')
            
            user = User.objects.create_user(username=nome,email=email,password=senha)
            user.save()
            messages.success(request, "Usuario criado com sucesso!")
            return redirect('usuarios:login')

        else:
            messages.error(request, "Não foi possivel realizar o cadastro!")      
            return redirect('usuarios:cadastro')

    else:
        cadastro_form = CadastroForm()
    
    return render(request, 'usuarios/cadastro.html', {
        "cadastro_form": cadastro_form,
    })

def logout(request):
    auth.logout(request)
    messages.success(request, "logout efetuado com sucesso!")
    return redirect('usuarios:login')