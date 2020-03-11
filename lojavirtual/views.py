from django.http import HttpResponse
from django.shortcuts import render

from .forms import ContactForm

def home_page(request):
    context = {
        "title": "Página principal",
        "content": "Seja bem-vindo a página principal",
    }
    return render(request, "home_page.html", context)

def about_page(request):
    context = {
        "title": "Página sobre",
        "content": "Seja bem-vindo a página sobre",
    }
    return render(request, "about/view.html", context)

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "Página contato",
        "content": "Seja bem-vindo a página contato",
        "form": contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    #if request.method == "POST":
        #print(request.POST)
        #print(request.POST.get('Nome_Completo'))
        #print(request.POST.get('email'))
        #print(request.POST.get('Mensagem'))
    return render(request, "contact/view.html", context)
