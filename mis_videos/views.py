#para hacer consulta usamos import psycopg2 y definimos las conexiones y el cursor para proceder a desarrollar las consultas
# Create your views here.
import re
from .models import Video,Usuario
from django.shortcuts import render,redirect
# redirect dirige el usuario a otra URL y se utiliza el request de la vista en la cual se ejecuta, redirige al usuario a otra URL o vista, como si se hiciera una nueva solicitud.
# render, renderiza una plantilla y la muestra en la misma solicitud
#Usa render cuando quieras presentar una página directamente, y redirect cuando sea necesario redirigir al usuario a otro lugar

class Validaciones():
    """
    Clase para realizar validaciones en diferentes elementos de entrada,
    como el ID de usuario, el nombre de usuario, el nombre del video, 
    la extensión del video y el tamaño del video.
    """

    def __init__(self, elemento_para_validar):
        """
        Inicializa la clase con el elemento que se va a validar.

        Args:
            elemento_para_validar (str): El elemento que se desea validar.
        """
        self.elemento_para_validar = elemento_para_validar
    
    def validar_usuario_id(self):
        """
        Valida que el ID de usuario sea alfanumérico (A-Z, a-z, 0-9).

        Returns:
            bool: True si el ID es válido, False si no lo es.
        """
        if re.fullmatch(r"[A-Za-z0-9]+", self.elemento_para_validar):
            return True
        print("Número de nómina inválido. Debe ser alfanumérico (A-Z, a-z, 0-9).")
        return False

    def validar_nombre_usuario(self):
        """
        Valida que el nombre del usuario contenga solo letras (A-Z, a-z).

        Returns:
            bool: True si el nombre es válido, False si no lo es.
        """
        if re.fullmatch(r"[A-Za-z]+", self.elemento_para_validar):
            return True
        print("Nombre del usuario inválido. Solo debe contener letras (A-Z, a-z).")
        return False

    def validar_nombre_video(self):
        """
        Valida que el nombre del video contenga solo caracteres alfanuméricos (A-Z, a-z, 0-9) y espacios.

        Returns:
            bool: True si el nombre del video es válido, False si no lo es.
        """
        if re.fullmatch(r"[A-Za-z0-9 ]+", self.elemento_para_validar):
            return True
        print("Nombre del video inválido. Debe ser alfanumérico (A-Z, a-z, 0-9).")
        return False

    def validar_extension_video(self):
        """
        Valida que la extensión del video sea alfanumérica seguida de '.com'.

        Returns:
            bool: True si la extensión es válida, False si no lo es.
        """
        if re.fullmatch(r"[A-Za-z0-9]+\.(com)", self.elemento_para_validar):
            return True
        print("Extensión del video inválida. Debe ser alfanómica seguida de '.com'.")
        return False

    def validar_tamaño(self):
        """
        Valida que el tamaño del video esté en el rango de 0 a 3.

        Returns:
            bool: True si el tamaño es válido, False si no lo es.
        """
        if self.elemento_para_validar != "":
            valor = float(self.elemento_para_validar)
            if valor <= 3 and valor > 0:
                return True
        print("Tamaño inválido. Debe ser un número entre 0 y 3.")
        return False

def index(request):
    """
    Vista para el formulario de entrada del usuario. Valida el ID y el nombre del usuario.

    Args:
        request (HttpRequest): La solicitud HTTP que contiene los datos del formulario.

    Returns:
        HttpResponse: La respuesta con el resultado de la validación y el renderizado de la página.
    """
    mensajeParaID = False
    mensajeParaNombre = False
    
    if request.method == "POST":
        # Obtener los datos del formulario
        usuario_id = request.POST.get("usuarioID")
        usuario_nombre = request.POST.get("usuarioNombre")
        if Validaciones(usuario_id).validar_usuario_id() == False:
            mensajeParaID = True
        if Validaciones(usuario_nombre).validar_nombre_usuario() == False:
            mensajeParaNombre = True

        # Si hay algún error de validación, renderiza con los mensajes de error
        if mensajeParaID or mensajeParaNombre:
            return render(request, "index.html", {
                "mensajeParaID": mensajeParaID,
                "mensajeParaNombre": mensajeParaNombre
            })

        # Crear o recuperar el usuario desde la base de datos
        usuario, existe = Usuario.objects.get_or_create(usuarioID=usuario_id, usuarioNombre=usuario_nombre)
        
        # Redirigir a la interfaz de usuario con el ID del usuario
        return redirect('interfazUsuario', user=usuario)
    
    return render(request, "index.html", {"mensajeParaID": mensajeParaID, "mensajeParaNombre": mensajeParaNombre})

def interfazUsuario(request, user):
    """
    Vista para la interfaz de usuario donde se gestionan los videos del usuario.

    Args:
        request (HttpRequest): La solicitud HTTP que contiene los datos del formulario.
        user (str): El ID del usuario cuya interfaz se está gestionando.

    Returns:
        HttpResponse: La respuesta con el renderizado de la página y los videos filtrados.
    """
    # Recuperar el usuario por su ID
    usuario = Usuario.objects.get(usuarioID=user)
    
    # Obtener los videos de ese usuario
    videos = Video.objects.filter(usuario=usuario)
    
    mensajeNombreVideo = False
    mensajeRutaVideo = False
    mensajeTamañoVideo = False
    
    if request.method == "POST":
        nombreVideo = request.POST.get("nombreVideo")
        rutaVideo = request.POST.get("rutaVideo")
        tamañoVideo = request.POST.get("videoTamaño")
        if Validaciones(nombreVideo).validar_nombre_video() == False:
            mensajeNombreVideo = True
        if Validaciones(rutaVideo).validar_extension_video() == False:
            mensajeRutaVideo = True
        if Validaciones(tamañoVideo).validar_tamaño() == False:
            mensajeTamañoVideo = True
        if mensajeNombreVideo or mensajeRutaVideo or mensajeTamañoVideo:
            return render(request, "interfazDeUsuario.html", {
                "videos": videos, 
                "mensajeNombreVideo": mensajeNombreVideo,
                "mensajeRutaVideo": mensajeRutaVideo,
                "mensajeTamañoVideo": mensajeTamañoVideo,   
            })
        # Validamos que todos los campos requeridos están completos
        # tamañoVideo = float(tamañoVideo)  # Convertimos a float si tiene valor válido
        # Crea y guarda el nuevo video en la base de datos
        nuevo_video = Video(
                videoNombre=nombreVideo,
                videoRuta=rutaVideo,
                videoTamaño=float(tamañoVideo),
                usuario=usuario  # Aquí estamos usando el objeto `usuario` recuperado
                )
        nuevo_video.save()
        return render(request, "interfazDeUsuario.html", {
                "videos": videos,   
            })
    # Renderizamos el HTML completo con el mensaje y los videos filtrados
    return render(request, "interfazDeUsuario.html", {
                "videos": videos,  
            })

def allVideos(request):
    """
    Vista para mostrar todos los videos almacenados en la base de datos.

    Args:
        request (HttpRequest): La solicitud HTTP que contiene la solicitud de todos los videos.

    Returns:
        HttpResponse: La respuesta con todos los videos mostrados.
    """
    videos = Video.objects.all()
    return render(request,"videos.html",{'videos':videos})

def eliminarVideo(request, NombreDelVideo):
    """
    Vista para eliminar un video específico basado en su nombre.

    Args:
        request (HttpRequest): La solicitud HTTP que contiene la solicitud de eliminación.
        NombreDelVideo (str): El nombre del video que se va a eliminar.

    Returns:
        HttpResponse: La respuesta redirigiendo a la interfaz de usuario del video eliminado.
    """
    video = Video.objects.get(videoNombre=NombreDelVideo)
    usuario = video.usuario  # Extraemos el id del usuario de la variable video
    video.delete()
    return redirect('interfazUsuario', user=usuario)
