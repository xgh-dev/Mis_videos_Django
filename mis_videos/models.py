from django.db import models
#py manage.py shell con esto abrimos la terminal
#from mis_videos.models import Usuario,Video asi importamos los modelos en la terminal
# ejemplo de llamar a los datos de un modelo  Usuario.objects.all()

# Create your models here.

# Datos del admin
# Username = admin
# Email address: admin@example.com
# Password: prueba123
# Password (again): prueba123
# Superuser created successfully.

class Usuario(models.Model):
    """
    Representa la tabla usuario en la base de datos.

    Atributos:
        usuarioID (str): Id del usuario.
        usuarioNombre (str): Nombre del usuario.
    """
    usuarioID = models.CharField(max_length=200, primary_key=True)
    usuarioNombre = models.CharField(max_length=200)

    def __str__(self):
        """
        Returas:
            str: El identificador único del usuario.
        """
        return self.usuarioID

    def retornarID(self):
        """
        Returna:
            str: El id del usuario.
        """
        return self.usuarioID

class Video(models.Model):
    """
    Representa la tabla video en la base de datos.

    Atributos:
        videoNombre (str): Nombre del video. Es clave primaria.
        videoRuta (str): Ruta donde se encuentra almacenado el video.
        videoTamaño (float): Tamaño del video en megabytes.
        usuario (ForeignKey): Relación con la clase Usuario que indica el dueño del video.
    """
    videoNombre = models.CharField(max_length=255, primary_key=True)
    videoRuta = models.CharField(max_length=500)
    videoTamaño = models.FloatField()
    usuario = models.ForeignKey(Usuario, to_field="usuarioID", on_delete=models.CASCADE)

    def __str__(self):
        """
        Returna:
            str: El nombre del video.
        """
        return self.videoNombre

    
