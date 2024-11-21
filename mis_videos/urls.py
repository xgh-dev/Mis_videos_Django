from django.urls import path

from . import views

# name = "nombre que hara referencia al tamplate"
"""
    En la variable urlpatterns se define las rutas URL para la aplicación y las asigna a las vistas correspondientes.
"""
urlpatterns = [
    path("", views.index, name="index"),
    path("videos/", views.allVideos, name="allVideos"),
    path("videos/<str:user>/", views.interfazUsuario, name="interfazUsuario"),
    path("videos/eliminar/<str:NombreDelVideo>/", views.eliminarVideo, name="eliminarVideo"),
]