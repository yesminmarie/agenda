from django.contrib import admin
from core.models import Evento

# Register your models here.


class EventoAdmin(admin.ModelAdmin):
    #mostra a listagem
    list_display = ('titulo', 'data_evento', 'data_criacao')
    list_filter = ('usuario', 'data_evento',) #cria um filtro


admin.site.register(Evento, EventoAdmin) #a classe Evento registra EventoAdmin
