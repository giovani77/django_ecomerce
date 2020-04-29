from django.db import models

class ProdutoManager(models.Manager):
    def get_by_id(self, id):
        qs = self.get_queryset().filter(id = id)
        if qs.count() == 1:
            return qs.first()
        return None

# Create your models here.
class Produto(models.Model): #produto_categoria
    nome        = models.CharField(max_length=120)
    descricao   = models.TextField()
    preco       = models.DecimalField(decimal_places=2, max_digits=20, default=100.00)
    imagem      = models.ImageField(upload_to = 'produtos/', null=True, blank=True)

    objects = ProdutoManager()
    
    #pythen 3
    def __str__(self):
        return self.nome

    #python 2
    def __unicode__(self):
        return self.nome