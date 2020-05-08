from django.urls import path

app_name = "produtos"

from .views import (
                        ProdutoListView, 
                        ProdutoDetailSlugView,
                    )

urlpatterns = [
    path('', ProdutoListView.as_view(), name='list'),
    path('<slug:slug>/', ProdutoDetailSlugView.as_view(), name='detail')
]