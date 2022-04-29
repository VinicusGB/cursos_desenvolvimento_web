from django.shortcuts import render

def index(request):
    return render(request,'index.html')

''' Função HttpResponse para enviar como resposta
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Receitas</h1>')
'''
