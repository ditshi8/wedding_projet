from django.urls import path
from .views import homeView
from .views import venteView
from .views import locationView
from .views import meetingView
from .views import contactView



urlpatterns = [
    path('', homeView, name = "index" ),
    path('vente/', venteView, name ="vente"),
    path('location/',locationView, name ="location"),
    path('meeting/', meetingView, name = "meeting"),
    path('contact/', contactView, name = "contact")
]