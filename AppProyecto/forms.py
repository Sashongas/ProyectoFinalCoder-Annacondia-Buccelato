from cProfile import label
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models.fields.files import ImageField

class PeliculaFormulario(forms.Form):
 tituloPeli = forms.CharField(max_length=50)
 generoPeli = forms.CharField(max_length=50)
 anioEstrenoPeli = forms.IntegerField()

class SerieFormulario(forms.Form):
    tituloSerie = forms.CharField(max_length=50)
    generoSerie = forms.CharField(max_length=50)
    anioEstrenoSerie = forms.IntegerField()

class DocumentalFormulario(forms.Form):
    tituloDoc = forms.CharField(max_length=50)
    generoDoc = forms.CharField(max_length=50)
    anioEstrenoDoc = forms.IntegerField()

class UserRegisterForm(UserCreationForm):
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget= forms.PasswordInput)
    password2 = forms.CharField(label="Repetir la Contraseña", widget= forms.PasswordInput)

    last_name = forms.CharField()
    first_name = forms.CharField()
    #imagen_avatar = forms.ImageField(required=False)

    class Meta: 
     model = User
     fields = ["username", "email", "password1", "password2", "last_name", "first_name"]
     help_texts = {k:"" for k in fields}
    
class UserEditForm(UserCreationForm):
    email = forms.EmailField(label = "Ingrese su email:")
    password1 = forms.CharField(label="Contraseña", widget= forms.PasswordInput)
    password2 = forms.CharField(label="Repetir la Contraseña", widget= forms.PasswordInput)

    class Meta: 
     model = User
     fields = ["email", "password1", "password2"]
     help_texts = {k:"" for k in fields}