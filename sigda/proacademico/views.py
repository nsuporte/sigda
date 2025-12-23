from django.shortcuts import redirect, render
from .models import Categoria, Obra, Arquivo, User

# Create your views here.

def index(request):
    obras = Obra.objects.all()
    return render(request, 'index.html', {'obras': obras})

def detalhe_obra(request, obra_id):
    obra = Obra.objects.get(id=obra_id)
    arquivos = Arquivo.objects.filter(obra=obra)
    return render(request, 'detalhe_obra.html', {'obra': obra, 'arquivos': arquivos})

def registar_obra(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        autor = User.objects.first()
        categoria_id = request.POST['categoria']
        categoria = Categoria.objects.get(id=categoria_id)
        ano_publicacao = request.POST['ano_publicacao']
        resumo = request.POST['resumo']
        
        nova_obra = Obra(
            titulo=titulo,
            autor=autor,
            categoria=categoria,
            ano_publicacao=ano_publicacao,
            resumo=resumo
        )
        nova_obra.save()
        return redirect('registar_arquivo', obra_id=nova_obra.id)
    else:
        categorias = Categoria.objects.all()
        return render(request, 'registar_obra.html', {'categorias': categorias})
    
def registar_arquivo(request, obra_id):
    obra = Obra.objects.get(id=obra_id)
    if request.method == 'POST':
        arquivo = request.FILES['arquivo']
        novo_arquivo = Arquivo(
            obra=obra,
            arquivo=arquivo
        )
        novo_arquivo.save()
        return redirect('registar_arquivo', obra_id=obra.id)
    else:
        obra = Obra.objects.get(id=obra_id)
        arquivos = Arquivo.objects.filter(obra=obra)
        return render(request, 'registar_arquivo.html', {'obra': obra, 'arquivos': arquivos})