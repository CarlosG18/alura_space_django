from django import forms

class LoginForm(forms.Form):
    nome = forms.CharField(
        max_length=100,
        label="Nome de Login",
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite seu Nickname",
            }
        )
    )
    senha = forms.CharField(
        max_length=100,
        label="Senha",
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha",
            }
        ),
    )

class CadastroForm(forms.Form):
    nome = forms.CharField(
        max_length=100,
        label="Nome Completo",
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite seu Nome completo",
            }
        )
    )

    email = forms.EmailField(
        label="Email",
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite seu email",
            }
        )
    )

    senha = forms.CharField(
        max_length=100,
        label="Senha",
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha",
            }
        ),
    )

    senha_confirmar = forms.CharField(
        max_length=100,
        label="Confirmação de senha",
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha mais uma vez",
            }
        ),
    )
    