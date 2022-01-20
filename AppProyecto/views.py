#from _typeshed import IdentityFunction
from urllib.request import Request
from django.shortcuts import render
from django.http import HttpResponse, response
from AppProyecto.forms import *
from AppProyecto.models import Pelicula, Documental, Serie
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from typing import List
from django.contrib.auth.decorators import login_required
from AppProyecto.forms import UserEditForm

# Create your views here.
def inicio(request):
    return render(request, 'AppProyecto/inicio.html')
    
def pelicula(request):
    
    if request.method == "POST":
     peliFormulario = PeliculaFormulario(request.POST)
     if peliFormulario.is_valid():
      informacion = peliFormulario.cleaned_data
      peliInsta = Pelicula(tituloPeli=informacion["tituloPeli"], generoPeli= informacion["generoPeli"], anioEstrenoPeli=informacion["anioEstrenoPeli"])
      peliInsta.save()
      return render(request, 'AppProyecto/inicio.html')
    
    else:
     peliFormulario = PeliculaFormulario()

    return render(request, 'AppProyecto/pelicula.html', {"peliFormulario":peliFormulario})
        

def serie(request):
    if request.method == "POST":
     serieFormulario = SerieFormulario(request.POST)
     if serieFormulario.is_valid():
      informacion = serieFormulario.cleaned_data
      serieInsta = Serie(tituloSerie=informacion["tituloSerie"], generoSerie=informacion["generoSerie"], anioEstrenoSerie=informacion["anioEstrenoSerie"])
      serieInsta.save()
      return render(request, 'AppProyecto/inicio.html')
    else:
     serieFormulario = SerieFormulario()
    return render(request, 'AppProyecto/serie.html', {"serieFormulario": serieFormulario})

def documental(request):
    if request.method == "POST":
     docFormulario = DocumentalFormulario(request.POST)
     if docFormulario.is_valid():
      informacion = docFormulario.cleaned_data
      docInsta = Documental(tituloDoc=informacion["tituloDoc"], generoDoc=informacion["generoDoc"], anioEstrenoDoc=informacion["anioEstrenoDoc"])
      docInsta.save()
      return render(request, 'AppProyecto/inicio.html')
    else:
     docFormulario = DocumentalFormulario
    return render(request, 'AppProyecto/documental.html', {"docFormulario": docFormulario})

#PELICULA

def busquedaPelicula(request):
    return render(request, 'AppProyecto/busquedaPelicula.html')

def buscarPelicula(request):
    if request.GET["tituloPeli"]:
     tituloPeli = request.GET["tituloPeli"]
     peliculas = Pelicula.objects.filter(tituloPeli__icontains=tituloPeli)
     return render(request, 'AppProyecto/resultadoBusquedaPeli.html', {"peliculas": peliculas, "tituloPeli": tituloPeli})
    else:
      respuesta = "Intentá de nuevo"
    return HttpResponse(respuesta)

#leerPelicula
#def leerPelicula(request):
    #peliculas = Pelicula.objects.all()
    #contexto = {"peliculas": peliculas}
    #return render(request, 'AppProyecto/leerPelicula.html', contexto)

def eliminarPelicula(request, peliParaBorrar): 
    peliculas = Pelicula.objects.get(tituloPeli = peliParaBorrar)
    peliculas.delete()

    peliculasTotal = Pelicula.objects.all()
    return render(request, 'AppProyecto/leerPelicula.html', {"peliculasTotal": peliculasTotal}) 

def editarPelicula(request, peliParaEditar):
    peli = Pelicula.objects.get(tituloPeli=peliParaEditar)

    if request.method == "POST":
        miFormulario = PeliculaFormulario(request.POST)
        if miFormulario.is_valid():
         info = miFormulario.cleaned_data
         
         peli.tituloPeli = info["tituloPeli"]
         peli.generoPeli = info["generoPeli"]
         peli.anioEstrenoPeli = info["anioEstrenoPeli"]
         
         peli.save()
         return render(request, 'AppProyecto/inicio.html')
    else:
     miFormulario = PeliculaFormulario(initial={"tituloPeli": peli.tituloPeli, "generoPeli": peli.generoPeli, "anioEstrenoPeli": peli.anioEstrenoPeli})
    return render(request, 'AppProyecto/editarPelicula.html', {"miFormulario": miFormulario, "peliParaEditar": peliParaEditar})


class PeliculaList(ListView):
    model = Pelicula
    template_name = "AppProyecto/pelicula_list.html"

class PeliculaDetalle(DetailView):
    model = Pelicula
    template_name = "AppProyecto/pelicula_detalle.html"

class PeliculaCreacion(CreateView):
    model = Pelicula
    success_url = "/AppProyecto/pelicula/list"
    fields = ["tituloPeli", "generoPeli", "anioEstrenoPeli"]

class PeliculaUpdate(UpdateView):
    model = Pelicula
    success_url = "/AppProyecto/pelicula/list"
    fields = ["tituloPeli", "generoPeli", "anioEstrenoPeli"]

class PeliculaDelete(DeleteView):
    model = Pelicula
    success_url = "/AppProyecto/pelicula/list"

def aboutUs(request):
    return render(request, 'AppProyecto/aboutUs.html')

#SERIE

def busquedaSerie(request):
    return render(request, 'AppProyecto/busquedaSerie.html')

def buscarSerie(request):
    if request.GET["tituloSerie"]:
     tituloSerie = request.GET["tituloSerie"]
     series = Serie.objects.filter(tituloSerie__icontains=tituloSerie)
     return render(request, 'AppProyecto/resultadoBusquedaSerie.html', {"series": series, "tituloSerie": tituloSerie})
    else:
      respuesta = "Intentá de nuevo"
    return HttpResponse(respuesta)

def leerSerie(request):
    series = Serie.objects.all()
    contexto = {"series": series}
    return render(request, 'AppProyecto/leerSerie.html', contexto)

def eliminarSerie(request, serieParaBorrar): 
    series = Serie.objects.get(tituloSerie = serieParaBorrar)
    series.delete()

    seriesTotal = Serie.objects.all()
    return render(request, 'AppProyecto/leerSerie.html', {"seriesTotal": seriesTotal})

def editarSerie(request, serieParaEditar):
    serie = Serie.objects.get(tituloSerie=serieParaEditar)

    if request.method == "POST":
        miFormulario = SerieFormulario(request.POST)
        if miFormulario.is_valid():
         info = miFormulario.cleaned_data
         
         serie.tituloSerie = info["tituloSerie"]
         serie.generoSerie = info["generoSerie"]
         serie.anioEstrenoSerie = info["anioEstrenoSerie"]
         
         serie.save()
         return render(request, 'AppProyecto/inicio.html')
    else:
     miFormulario = SerieFormulario(initial={"tituloSerie": serie.tituloSerie, "generoSerie": serie.generoSerie, "anioEstrenoSerie": serie.anioEstrenoSerie})
    return render(request, 'AppProyecto/editarSerie.html', {"miFormulario": miFormulario, "serieParaEditar": serieParaEditar})

class SerieList(ListView):
    model = Serie
    template_name = "AppProyecto/serie_list.html"

class SerieDetalle(DetailView):
    model = Serie
    template_name = "AppProyecto/serie_detalle.html"

class SerieCreacion(CreateView):
    model = Serie
    success_url = "/AppProyecto/serie/list"
    fields = ["tituloSerie", "generoSerie", "anioEstrenoSerie"]

class SerieUpdate(UpdateView):
    model = Serie
    success_url = "/AppProyecto/serie/list"
    fields = ["tituloSerie", "generoSerie", "anioEstrenoSerie"]

class SerieDelete(DeleteView):
    model = Serie
    success_url = "/AppProyecto/serie/list"

#DOCU

def busquedaDoc(request):
    return render(request, 'AppProyecto/busquedaDoc.html')

def buscarDoc(request):
    if request.GET["tituloDoc"]:
     tituloDoc = request.GET["tituloDoc"]
     docs = Documental.objects.filter(tituloDoc__icontains=tituloDoc)
     return render(request, 'AppProyecto/resultadoBusquedaDoc.html', {"docs": docs, "tituloDoc": tituloDoc})
    else:
      respuesta = "Intentá de nuevo"
    return HttpResponse(respuesta)

def leerDoc(request):
    docs = Documental.objects.all()
    contexto = {"docs": docs}
    return render(request, 'AppProyecto/leerDoc.html', contexto)

def eliminarDoc(request, docParaBorrar): 
    docs = Documental.objects.get(tituloDoc = docParaBorrar)
    docs.delete()

    docsTotal = Documental.objects.all()
    return render(request, 'AppProyecto/leerDoc.html', {"docsTotal": docsTotal})

def editarDoc(request, docParaEditar):
    doc = Documental.objects.get(tituloDoc=docParaEditar)

    if request.method == "POST":
        miFormulario = DocumentalFormulario(request.POST)
        if miFormulario.is_valid():
         info = miFormulario.cleaned_data
         
         doc.tituloDoc = info["tituloDoc"]
         doc.generoDoc = info["generoDoc"]
         doc.anioEstrenoDoc = info["anioEstrenoDoc"]
         
         doc.save()
         return render(request, 'AppProyecto/inicio.html')
    else:
     miFormulario = DocumentalFormulario(initial={"tituloDoc": doc.tituloDoc, "generoDoc": doc.generoDoc, "anioEstrenoDoc": doc.anioEstrenoDoc})
    return render(request, 'AppProyecto/editarDoc.html', {"miFormulario": miFormulario, "docParaEditar": docParaEditar})

class DocList(ListView):
    model = Documental
    template_name = "AppProyecto/doc_list.html"

class DocDetalle(DetailView):
    model = Documental
    template_name = "AppProyecto/doc_detalle.html"

class DocCreacion(CreateView):
    model = Documental
    success_url = "/AppProyecto/doc/list"
    fields = ["tituloDoc", "generoDoc", "anioEstrenoDoc"]

class DocUpdate(UpdateView):
    model = Documental
    success_url = "/AppProyecto/doc/list"
    fields = ["tituloDoc", "generoDoc", "anioEstrenoDoc"]

class DocDelete(DeleteView):
    model = Documental
    success_url = "/AppProyecto/doc/list"

#LOGIN
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
          usuario = form.cleaned_data.get("username")
          contrasenia = form.cleaned_data.get("password")
          user = authenticate(username=usuario, password=contrasenia)
          if user is not None:
              login(request, user)
              return render(request, 'AppProyecto/inicio.html', {"mensaje": f"Bienvenido {usuario}"})
          else:
              return render(request, 'AppProyecto/inicio.html', {"mensaje": "Error, datos incorrectos"})
        else: 
          return render(request, 'AppProyecto/inicio.html', {"mensaje": "Error, formulario erroneo"})   
    form = AuthenticationForm()
    return render(request, 'AppProyecto/login.html', {"form": form})

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()

            return render(request, 'AppProyecto/inicio.html', {"mensaje": f"Usuario creado :) {username}"})
    else:
        form = UserRegisterForm()
    return render(request, 'AppProyecto/register.html', {"form": form})



#LEER PELICULA, login required
@login_required
def leerPelicula(request):
    peliculas = Pelicula.objects.all()
    contexto = {"peliculas": peliculas}
    return render(request, 'AppProyecto/leerPelicula.html', contexto)

#EDITAR PERFIL, login required
@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST)
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            usuario.email = info['email']
            usuario.password1 = info['password1']
            usuario.password2 = info['password2']

            usuario.save()
            return render(request, 'AppProyecto/inicio.html')
    else:
        miFormulario = UserEditForm(initial = {'email':usuario.email})
    return render(request, 'AppProyecto/editarPerfil.html', {"miFormulario": miFormulario, "usuario": usuario})
