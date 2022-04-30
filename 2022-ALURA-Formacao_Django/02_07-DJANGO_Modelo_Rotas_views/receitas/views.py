import re
from django.shortcuts import render

def index(request):
    receitas = {
        1:'Lasanha',
        2:'Sopa de legumes',
        3:'Sorvete'
    }
    dados = {
        'nome_das_receitas': receitas
    }
    return render(request,'index.html',dados)

def receita(request):
    return render(request,'receita.html')

''' Função HttpResponse para enviar como resposta
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Receitas</h1>')
'''
