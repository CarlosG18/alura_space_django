from django.db import models
from datetime import datetime

# Create your models here.
class Fotografia(models.Model):
    CATEGORIA_CHOISES = [
        ("NEBULOSA", "nebulosa"),
        ("ESTRELA", "estrela"),
        ("GALÁXIA", "galáxia"),
        ("PLANETA", "planeta"),
    ]

    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=200, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=CATEGORIA_CHOISES, default='')
    descricao = models.TextField(null=False, blank=False)
    data = models.DateTimeField(default=datetime.now, blank=False)
    foto = models.ImageField(upload_to='galeria/', blank=True)
    publicada = models.BooleanField(default=False)

    def __str__(self):
        return f'Fotografia [nome={self.nome}]'