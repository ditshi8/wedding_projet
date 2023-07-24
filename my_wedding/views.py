from django.shortcuts import render
from .models import Article

# Create your views here.

def homeView(request, template_name="wedding/pages/index.html"):

    #context permet à envoyer le code python vers le html
    #declaration du context
    context = {}
    bonjour = "bonjour tout le monde "

    #affectation de la cléf et de la valeur dans le context
    #           key     value
    context['name'] = bonjour

    # instance de l'article
    a1 = Article("Robes bustiers", "Robes bustiers description" )
    a2 = Article("Robes singets", "description" )
    a3 = Article("Robes dentellées", "description" )
    a4 = Article("voilles", "description" )
    list_article = [a1, a2, a3, a4]
    #for art in list_article:
        #print(art.title)
    print(a1.title)
    context['article'] = list_article


    return render(request, template_name,context)

def venteView(request, template_name="wedding/pages/vente.html"):
    return render(request, template_name)

def locationView(request, template_name="wedding/pages/location.html"):
    return render(request,template_name)

def meetingView(request, template_name="wedding/pages/meeting.html"):
    return render(request,template_name)

def contactView(request, template_name="wedding/pages/contact.html"):
    return render(request, template_name)