from django.shortcuts import render

# Create your views here.

def design_limitada_index(request):
    return render(
        request,
        "index.html"
    )

def design_limitada_elementos_de_design(request):
    return render(
        request,
        "elementos_de_design.html"
    )

def design_limitada_contatos(request):
    return render(
        request,
        "contatos.html"
    )