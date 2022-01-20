from unicodedata import name
from django.urls import path,re_path
from AppProyecto import views
from AppProyecto.views import busquedaPelicula, login_request
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('inicio', views.inicio, name = "Inicio"),
    path('pelicula', views.pelicula, name = "Pelicula"),
    path('serie', views.serie, name = "Serie"),
    path('documental', views.documental, name = "Documental"),
   
    path('busquedaPelicula', views.busquedaPelicula),
    path('buscarPelicula/', views.buscarPelicula),
    path('leerPelicula', views.leerPelicula, name = "LeerPelicula"),
    path('eliminarPelicula/<peliParaBorrar>/', views.eliminarPelicula, name = "EliminarPelicula"),
    path('editarPelicula/<peliParaEditar>/', views.editarPelicula, name = "EditarPelicula"),
    path('pelicula/list', views.PeliculaList.as_view(), name = 'List'),
    re_path(r'^(?P<pk>\d+)$', views.PeliculaDetalle.as_view(), name = 'Detail'),
    re_path(r'^nuevo$', views.PeliculaCreacion.as_view(), name = 'New'),
    re_path(r'^editar/(?P<pk>\d+)$', views.PeliculaUpdate.as_view(), name = 'Edit'),
    re_path(r'^borrar/(?P<pk>\d+)$', views.PeliculaDelete.as_view(), name = 'Delete'),    

    path('busquedaSerie', views.busquedaSerie),
    path('buscarSerie/', views.buscarSerie),
    path('leerSerie', views.leerSerie, name = "LeerSerie"),
    path('eliminarSerie/<serieParaBorrar>/', views.eliminarSerie, name = "EliminarSerie"),
    path('editarSerie/<serieParaEditar>/', views.editarSerie, name = "EditarSerie"),
   
    path('serie/list', views.SerieList.as_view(), name = 'ListSerie'),
    re_path(r'^(?P<pk>\d+)$', views.SerieDetalle.as_view(), name = 'DetailSerie'),
    re_path(r'^nuevo$', views.SerieCreacion.as_view(), name = 'NewSerie'),
    re_path(r'^editar/(?P<pk>\d+)$', views.SerieUpdate.as_view(), name = 'EditSerie'),
    re_path(r'^borrar/(?P<pk>\d+)$', views.SerieDelete.as_view(), name = 'DeleteSerie'),  

    path('busquedaDoc', views.busquedaDoc),
    path('buscarDoc/', views.buscarDoc),
    path('leerDoc', views.leerDoc, name = "LeerDoc"),
    path('eliminarDoc/<docParaBorrar>/', views.eliminarDoc, name = "EliminarDoc"),
    path('editarDoc/<docParaEditar>/', views.editarDoc, name = "EditarDoc"),

    path('doc/list', views.DocList.as_view(), name = 'ListDoc'),
    re_path(r'^(?P<pk>\d+)$', views.DocDetalle.as_view(), name = 'DetailDoc'),
    re_path(r'^nuevo$', views.DocCreacion.as_view(), name = 'NewDoc'),
    re_path(r'^editar/(?P<pk>\d+)$', views.DocUpdate.as_view(), name = 'EditDoc'),
    re_path(r'^borrar/(?P<pk>\d+)$', views.DocDelete.as_view(), name = 'DeleteDoc'), 

    path('login', views.login_request, name = "Login"),
    path('register', views.register, name = "Register"),
    path('logout', LogoutView.as_view(template_name = 'AppProyecto/logout.html'), name = "Logout"),
    path('editarPerfil', views.editarPerfil, name = "EditarPerfil"),

    path('aboutUs', views.aboutUs, name = "AboutUs")
]