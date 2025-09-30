from django.shortcuts import render
from django.contrib.auth.decorators import login_required 
# Create your views here.
@login_required
def dashboard(request):
    return render(request, "conteudo/dashboard.html")

@login_required
def terrenos(request):
    return render(request, "conteudo/terrenos.html")

@login_required
def clima(request):
    return render(request, "conteudo/clima.html")

@login_required
def calculadora(request):
    return render(request, "conteudo/calculadora.html")

@login_required
def recomendacoes(request):
    return render(request, "conteudo/recomendacoes.html")

@login_required
def produtos(request):
    return render(request, "conteudo/produtos.html")

@login_required
def dicas(request):
    return render(request, "conteudo/dicas.html")

@login_required
def contatos(request):
    return render(request, "conteudo/contatos.html")