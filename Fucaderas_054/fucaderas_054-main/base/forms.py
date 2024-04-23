from django import forms
from .models import Carrinho

class AdicionarCarrinhoForm(forms.ModelForm):
    class Meta:
        model = Carrinho
        fields = ('nome', 'preco','quantidade','imagem')