from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def ENTRAR(request):
    return HttpResponse('Pagina de login')