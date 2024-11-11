from django.db import models
#py manage.py shell con esto abrimos la terminal
#from mis_videos.models import Usuario,Video asi importamos los modelos en la terminal
# ejemplo de llamar a los datos de un modelo  Usuario.objects.all()

# Create your models here.

# Username = adnim
# Email address: admin@example.com
# Password: xgh270999
# Password (again): xgh270999
# Superuser created successfully.

class Usuario(models.Model):
    usuarioID = models.CharField(max_length=200, primary_key=True)  # Campo de clave primaria
    usuarioNombre = models.CharField(max_length=200)

    def __str__(self):
        return self.usuarioID
    def retornarID(self):
        return self.usuarioID

class Video(models.Model):
    videoNombre = models.CharField(max_length=255,primary_key=True)  # Nombre del video
    videoRuta = models.CharField(max_length=500)    # Ruta del video
    videoTamaño = models.FloatField()               # Tamaño del video en MB o GB
    usuario = models.ForeignKey(Usuario, to_field="usuarioID", on_delete=models.CASCADE)  # Relación con Usuario

    def __str__(self):
        return self.videoNombre
    #def retornarUsuario(self):
    #    return self.usuario.usuarioID
    
