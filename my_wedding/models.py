from django.db import models

# Create your models here.
# je suis un commentaire


class Article(models.Model):

    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    images = models.ImageField(default='article/')
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    publication = models.BooleanField()

    def __str__(self):
     return self.title

class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    content = models.TextField()

    #cette fonction permet à retourner nos informations inserées
    def __str__(self):
        return f'{self.name} {self.email}'

