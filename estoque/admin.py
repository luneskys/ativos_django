from django.contrib import admin
from .models import Ativo

@admin.register(Ativo)
class AtivoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'numero_patrimonio', 'categoria', 'status', 'localizacao')
    search_fields = ('nome', 'numero_patrimonio', 'categoria')
    list_filter = ('status', 'categoria')
