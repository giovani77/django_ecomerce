from django.views.generic import ListView, DetailView
from django.shortcuts import render

from .models import Produto

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


#Class Based View
class ProdutoDetailView(DetailView):
    #traz todos os produtos do banco de dados sem filtrar nada 
    queryset = Produto.objects.all()
    template_name = "produtos/detail.html"
    
    #def get_context_data(self, *args, **kwargs):
        #context = super(ProdutoDetailView, self).get_context_data(*args, **kwargs)
        #print(context)
        #return context

#Function Based View
def produto_detail_view(request):
    queryset = Produto.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "produtos/detail.html", context)