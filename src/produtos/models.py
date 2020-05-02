from django.db import models

#Custom queryset
class ProdutoQuerySet(models.query.QuerySet):
    def ehProdutoAtivo(self):
        return self.filter(ehProdutoAtivo = True)

    def ehDestaque(self):
        return self.filter(ehDestaque = True, ehProdutoAtivo = True)

class ProdutoManager(models.Manager):
    def get_queryset(self):
        return ProdutoQuerySet(self.model, using = self._db)
    
    def all(self):
        return self.get_queryset().ehProdutoAtivo()

    def ehDestaque(self):
        #return self.get_queryset().filter(ehDestaque = True)
        return self.get_queryset().ehDestaque()
    
    def get_by_id(self, id):
        qs = self.get_queryset().filter(id = id)
        if qs.count() == 1:
            return qs.first()
        return None

# Create your models here.
class Produto(models.Model): #produto_categoria
    nome            = models.CharField(max_length=120)
    slug            = models.SlugField()
    descricao       = models.TextField()
    preco           = models.DecimalField(decimal_places=2, max_digits=20, default=100.00)
    imagem          = models.ImageField(upload_to = 'produtos/', null=True, blank=True)
    ehDestaque      = models.BooleanField(default = False)
    ehProdutoAtivo  = models.BooleanField(default = True)

    objects = ProdutoManager()
    
    #pythen 3
    def __str__(self):
        return self.nome

    #python 2
    def __unicode__(self):
        return self.nome