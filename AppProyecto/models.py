from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Pelicula(models.Model):
    tituloPeli = models.CharField(max_length=50)
    generoPeli = models.CharField(max_length=50)
    anioEstrenoPeli = models.IntegerField()

    def __str__(self):
     return f"Título: {self.tituloPeli} (Año {self.anioEstrenoPeli})"

class Serie(models.Model):
    tituloSerie = models.CharField(max_length=50)
    generoSerie = models.CharField(max_length=50)
    anioEstrenoSerie = models.IntegerField()

    def __str__(self):
     return f"Título: {self.tituloSerie} (Año {self.anioEstrenoSerie})"

class Documental(models.Model):
    tituloDoc = models.CharField(max_length=50)
    generoDoc = models.CharField(max_length=50)
    anioEstrenoDoc = models.IntegerField()

    def __str__(self):
     return f"Título: {self.tituloDoc} (Año {self.anioEstrenoDoc})"
