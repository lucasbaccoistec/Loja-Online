from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

class Vendedor(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    data_de_criacao = models.DateTimeField(auto_now_add=True)

class Artigo(models.Model):
    nome = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField()
    data_de_criacao = models.DateTimeField(auto_now_add=True)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE, related_name='artigos')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='artigos')