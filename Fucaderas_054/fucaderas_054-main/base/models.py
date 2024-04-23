from django.db import models

# Create your models here.
class Product(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    imagem_front = models.ImageField(upload_to='products')
    imagem_back = models.ImageField(upload_to='products')
    quantidade = models.IntegerField(default=0)

    def __str__(self):
        return self.nome