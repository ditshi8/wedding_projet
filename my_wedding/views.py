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
    #SELECT * FROM ARTICLE , with SQL
    # With ORM
    list_article = Article.objects.all()
    #for art in list_article:
        #print(art.title)
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