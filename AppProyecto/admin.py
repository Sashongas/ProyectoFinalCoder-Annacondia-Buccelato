from django.contrib import admin

# Register your models here.
from AppProyecto.models import *

admin.site.register(Pelicula)
admin.site.register(Serie)
admin.site.register(Documental)

