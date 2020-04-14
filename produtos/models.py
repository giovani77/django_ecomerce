from django.db import models

# Create your models here.
class Produto(models.Model): #produto_categoria
    nome        = models.CharField(max_length=120)
    descricao   = models.TextField()
    preco       = models.DecimalField(decimal_places=2, max_digits=20, default=100.00)

    #pythen 3
    def __str__(self):
        return self.nome