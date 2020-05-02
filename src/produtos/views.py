from django.http import Http404
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404

from .models import Produto

class ProdutoEhDestaqueListView(ListView):
    template_name = "produtos/list.html"
    
    def get_queryset(self, *args, **kwargs):
        return Produto.objects.ehDestaque()

class ProdutoEhDestaqueDetailView(DetailView):
    queryset = Produto.objects.all().ehDestaque()
    template_name = "produtos/destaque-detail.html"

    # def get_queryset(self, *args, **kwargs):
    #    request = self.request
    #    return Produto.objects.ehDestaque()

#Class Based View
class ProdutoListView(ListView):
    #traz todos os produtos do banco de dados sem filtrar nada
    queryset = Produto.objects.all()
    template_name = "produtos/list.html"
    
    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProdutoListView, self).get_context_data(*args, **kwargs)
    #     print(context)
    #     return context

#Function Based View
def produto_list_view(request):
    queryset = Produto.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "produtos/list.html", context)

class ProdutoDetailSlugView(DetailView):
    queryset = Produto.objects.all()
    template_name = "produtos/detail.html"

    def get_object(self, *args, **kwargs):
        slug = self.kwargs.get('slug')
        #instance = get_object_or_404(Produto, slug = slug, active = True)
        try:
            instance = Produto.objects.get(slug = slug, ehProdutoAtivo = True)
        except Produto.DoesNotExist:
            raise Http404("Não encontrado!")
        except Produto.MultipleObjectsReturned:
            qs = Produto.objects.filter(slug = slug, ehProdutoAtivo = True)
            instance =  qs.first()
        return instance

#Class Based View
class ProdutoDetailView(DetailView):
    #traz todos os produtos do banco de dados sem filtrar nada 
    #queryset = Produto.objects.all()
    template_name = "produtos/detail.html"
    
    def get_context_data(self, *args, **kwargs):
        context = super(ProdutoDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context

    def get_object(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        instance = Produto.objects.get_by_id(pk)
        if instance is None:
            raise Http404("Esse produto não existe!")
        return instance

#Function Based View
def produto_detail_view(request, pk = None, *args, **kwargs):
    instance = Produto.objects.get_by_id(pk)
    print(instance)
    if instance is None:
        raise Http404("Esse produto não existe!")

    context = {
        'object': instance
    }
    return render(request, "produtos/detail.html", context)