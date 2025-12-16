from django.shortcuts import render
from .models import Categoria, Obra, Arquivo

# Create your views here.
def index(request):
    obras = Obra.objects.all()
    return render(request, 'index.html', {'obras': obras})

def registar(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        autor = request.user
        categoria_id = request.POST.get('categoria')
        categoria = Categoria.objects.get(id=categoria_id)
        ano_publicacao = request.POST.get('ano_publicacao')
        resumo = request.POST.get('resumo')

        obra = Obra.objects.create(
            titulo=titulo,
            autor=autor,
            categoria=categoria,
            ano_publicacao=ano_publicacao,
            resumo=resumo
        )

        return render(request, 'index.html', {'obra': obra})

    categorias = Categoria.objects.all()
    return render(request, 'registar.html', {'categorias': categorias})

def detalhe(request, obra_id):
    obra = Obra.objects.get(id=obra_id)
    arquivos = Arquivo.objects.filter(obra=obra)
    return render(request, 'detalhe.html', {'obra': obra, 'arquivos': arquivos})



    