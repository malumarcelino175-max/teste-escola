from django.shortcuts import render

# Create your views here.

def lista_view(request):
    return render(request, "alunos/lista.html")

def novo_view(request):
    return render(request, "alunos/novo.html")

def detalhe_view(request):
    return render(request, "alunos/detalhe.html")