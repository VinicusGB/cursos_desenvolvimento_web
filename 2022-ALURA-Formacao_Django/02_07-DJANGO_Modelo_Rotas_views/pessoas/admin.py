from csv import list_dialects
from django.contrib import admin
from .models import Pessoa

class ListandoPessoas(admin.ModelAdmin):
    list_display = ('id','nome','email')
    list_display_link = ('nome','email')
    search_fields = ('nome',)
    list_per_page = 10

admin.site.register(Pessoa, ListandoPessoas)
