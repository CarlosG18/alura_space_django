from django import forms
from .models import Fotografia

class FotografiaForm(forms.ModelForm):
    class Meta:
        model = Fotografia
        exclude = ("publicada","usuario")

        labels = {
            "descricao": "Descrição",
        }

        widgets = {
            "nome": forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite o Nome da imagem",
                }
            ),
            "legenda": forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite a legenda da imagem",
                }
            ),
            "categoria": forms.Select(
            attrs={
                "class": "form-control",
                }
            ),
            "descricao": forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Digite a descricao da foto",
            }
            ),
            "foto": forms.FileInput(
            attrs={
                "class": "form-control",
            }
            ),
            "data": forms.DateInput(
            format= '%d/%m/%Y',
            attrs={
                "class": "form-control",
                "type": 'date',
            }
            )
        }
