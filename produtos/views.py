from django.views.generic import ListView
from django.shortcuts import render

from .models import Produto

#Class Based View
class ProdutoListView(ListView):
    #traz todos os produtos do banco de dados sem filtrar nada
    queryset = Produto.objects.all()
    template_name = "produtos/list.html"

#Function Based View
def produto_list_view(request):
    queryset = Produto.objects.all()
    context = {
        'qs': queryset
    }
    return render(request, "produtos/list.html", context)

