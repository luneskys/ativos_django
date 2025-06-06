from django.contrib import admin
from .models import Ativo

@admin.register(Ativo)
class AtivoAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'nome', 'numero_patrimonio', 'status')
    search_fields = ('tipo', 'nome', 'numero_patrimonio', 'serial_number')
    list_filter = ('status',)

