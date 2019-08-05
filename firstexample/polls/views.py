from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    response = "Olá, mundo! Bem-vindos à primeira aplicação."
    return HttpResponse(response)
