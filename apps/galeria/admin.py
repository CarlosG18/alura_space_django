from django.contrib import admin
from .models import Fotografia

class FotografiaConfigs(admin.ModelAdmin):
    list_display = ("id", "nome", "categoria", "data", "usuario", "publicada")
    list_display_links = ["nome"]
    search_fields = ["nome", "legenda"]
    list_filter = ["categoria", "data","usuario"]
    list_per_page = 5
    list_editable = ["publicada"]

# Register your models here.
admin.site.register(Fotografia, FotografiaConfigs)
