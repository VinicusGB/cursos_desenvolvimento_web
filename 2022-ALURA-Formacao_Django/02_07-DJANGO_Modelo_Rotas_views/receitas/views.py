import re
from django.shortcuts import get_object_or_404, render
from .models import Receita

def index(request):
    receitas = Receita.objects.all()
    dados = {
        'receitas': receitas
    }
    return render(request,'index.html',dados)

def receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)

    receita_a_exibir = {
        'receita' : receita
    }

    return render(request,'receita.html',receita_a_exibir)

''' Função HttpResponse para enviar como resposta
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Receitas</h1>')
'''
