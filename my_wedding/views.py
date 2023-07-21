from django.shortcuts import render

# Create your views here.

def homeView(request, template_name="wedding/index.html"):

    #context permet à envoyer le code python vers le html
    #declaration du context
    context = {}
    bonjour = "bonjour tout le monde "

    #affectation de la cléf et de la valeur dans le context
    #           key     value
    context ['name'] = bonjour

    return render(request, template_name,context)
