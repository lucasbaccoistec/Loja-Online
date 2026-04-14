from django.shortcuts import render, get_object_or_404
from .models import Artigo, Categoria, Vendedor

def lista_artigos(request):
    artigos = Artigo.objects.all().order_by('-data_de_criacao')
    return render(request, 'loja/lista_artigos.html', {'artigos': artigos})

def artigos_por_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    artigos = categoria.artigos.all()
    return render(request, 'loja/artigos_categoria.html', {'categoria': categoria, 'artigos': artigos})

def perfil_vendedor(request, vendedor_id):
    vendedor = get_object_or_404(Vendedor, id=vendedor_id)
    return render(request, 'loja/perfil_vendedor.html', {'vendedor': vendedor})