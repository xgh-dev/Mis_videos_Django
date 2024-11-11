from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("videos/", views.allVideos, name="allVideos"),
    path("videos/<str:user>/", views.interfazUsuario, name="interfazUsuario"),
    path("videos/eliminar/<str:NombreDelVideo>/", views.eliminarVideo, name="eliminarVideo"),
]
