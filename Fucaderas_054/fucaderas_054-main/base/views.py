from django.shortcuts import render
from .models import Product
from django.http import JsonResponse

  

# Create your views here.

def inicio(request):
    return render ( request, 'base.html')

def produtos(request):
    return render ( request, 'produtos.html')


#criar views para o carrinho de compras para atualizar o carrinho no template
def carrinho_compras(request):
    produtos_no_carrinho = Product.objects.filter(quantidade__gt=0)
    total_produtos_no_carrinho = produtos_no_carrinho.count()
    return render(request, 'carrinho_compras.html', {'produtos_no_carrinho':produtos_no_carrinho, 'total_produtos_carrinho':total_produtos_no_carrinho})

#criar views para processar o envio dos dados dos produtos

def adicionar_produto(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        preco = request.POST.get('preco')
        imagem_front = request.POST.get('imagem_front')
        imagem_back = request.POST.get('imagem_back')

        product = Product.objects.create(nome=nome, preco=preco, imagem_front=imagem_front, imagem_back=imagem_back)
        return JsonResponse({'message': 'Produto adicionado com sucesso!'})
    else:
        return JsonResponse({'error': 'Método não permitido'}, status=405)

def galeria(request):
    return render ( request, 'galeria.html')



