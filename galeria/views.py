from django.shortcuts import render
from .models import Perfil, Experiencia, Projeto

def index(request):
    perfil_dados = Perfil.objects.first()
    experiencias_dados = Experiencia.objects.all()
    projetos_dados = Projeto.objects.all()

    contexto = {
        'perfil': perfil_dados,
        'experiencia': experiencias_dados,
        'projetos': projetos_dados
    }

    return render(request, 'galeria/index.html',contexto)