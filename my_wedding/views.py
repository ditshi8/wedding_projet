from django.shortcuts import render, redirect
from .models import Article
from .models import Contact


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
    context = {}
    # SELECT * FROM Contact
    contacts = Contact.objects.all()
    # recuperer la liste de nos contacts
    context["contacts"] = contacts

    # verification de la methode de la requele == POST
    if request.method == "POST":
        #Recuperation des valeur entrées par l'utilisateur
        name = request.POST['name']
        email = request.POST['email']
        content = request.POST['content']



        # creation de notre objet Contact
        obj_contact = Contact(
            name = name,
            email = email,
            content = content
        )

        obj_contact.save()


    return render(request, template_name, context)

def gestionContactView(request, template_name = "wedding/pages/gestionContact.html"):
    context = {}
    # SELECT * FROM Contact
    contacts = Contact.objects.all()
    # recuperer la liste de nos contacts
    context["contacts"] = contacts

    if request.method == "POST":
        # Recuperation des valeur entrées par l'utilisateur
        name = request.POST['name']
        email = request.POST['email']
        content = request.POST['content']

        # creation de notre objet Contact
        obj_contact = Contact(
            name=name,
            email=email,
            content=content
        )

        obj_contact.save()

    return render(request, template_name, context)

# Foction update

def uptateContactView(request, contact_id ,template_name="wedding/pages/gestionContact.html"):
    contact_one = Contact.objects.get(id=contact_id)
    print("id", contact_one)
    context = {}
    contacts = Contact.objects.all()
    context['contacts'] = contacts
    context['contact_one'] = contact_one
    #verifie si la condition == POST
    if request.method == "POST":
        # recuperation des donnees qui se trouve dans l'input et on le modifie
        name = request.POST['name']
        email = request.POST['email']
        content = request.POST['content']
        #assigner les valeur de l'input
        contact_one.name = name
        contact_one.email = email
        contact_one.content = content
        #sauvegarde de la modification
        contact_one.save()

    return  render(request,  template_name, context)

def deleteContactView(request, contact_id):
    contact_one = Contact.objects.get(id=contact_id)
    contact_one.delete()

    return redirect('gestion_contact')


