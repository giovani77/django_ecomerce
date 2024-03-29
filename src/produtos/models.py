from django.db import models
from .utils import unique_slug_generator
from django.db.models.signals import pre_save
from django.urls import reverse

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
    slug            = models.SlugField(blank = True, unique = True)
    descricao       = models.TextField()
    preco           = models.DecimalField(decimal_places=2, max_digits=20, default=100.00)
    imagem          = models.ImageField(upload_to = 'produtos/', null=True, blank=True)
    ehDestaque      = models.BooleanField(default = False)
    ehProdutoAtivo  = models.BooleanField(default = True)
    timestamp       = models.DateTimeField(auto_now_add = True)

    objects = ProdutoManager()
    
    def get_absolute_url(self):
        #return "/produtos/{slug}/".format(slug = self.slug)
        return reverse("produtos:detail", kwargs={"slug": self.slug})

    #pythen 3
    def __str__(self):
        return self.nome

    #python 2
    def __unicode__(self):
        return self.nome

def produto_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(produto_pre_save_receiver, sender = Produto)