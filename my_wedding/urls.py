from django.urls import path
from .views import homeView
from .views import venteView
from .views import locationView
from .views import meetingView
from .views import contactView
from .views import gestionContactView
from .views import uptateContactView
from .views import deleteContactView



urlpatterns = [
    path('', homeView, name = "index" ),
    path('vente/', venteView, name ="vente"),
    path('location/',locationView, name ="location"),
    path('meeting/', meetingView, name = "meeting"),
    path('contact/', contactView, name = "contact"),
    path('gestion-contact/', gestionContactView, name = "gestion_contact"),
    path('gestion-contact/update/<int:contact_id>/', uptateContactView, name = "update_contact"),
    path('gestion-contact/delete/<int:contact_id>/', deleteContactView, name = "delete_contact")

]