#para hacer consulta usamos import psycopg2 y definimos las conexiones y el cursor para proceder a desarrollar las consultas
# Create your views here.
import re
from .models import Video,Usuario
from django.shortcuts import render,redirect
# redirect dirige el usuario a otra URL y se utiliza el request de la vista en la cual se ejecuta, redirige al usuario a otra URL o vista, como si se hiciera una nueva solicitud.
# render, renderiza una plantilla y la muestra en la misma solicitud
#Usa render cuando quieras presentar una página directamente, y redirect cuando sea necesario redirigir al usuario a otro lugar

class Validaciones():
    def __init__(self,elemento_para_validar):
        self.elemento_para_validar = elemento_para_validar
    
    def validar_usuario_id(self):
        #Valor alfanumérico (A-Z, a-z, 0-9)
        if re.fullmatch(r"[A-Za-z0-9]+", self.elemento_para_validar):
            return True
        print("Número de nómina inválido. Debe ser alfanumérico (A-Z, a-z, 0-9).")
        return False

    def validar_nombre_usuario(self):
        #Valor alfabético (A-Z, a-z)
        if re.fullmatch(r"[A-Za-z]+", self.elemento_para_validar):
            return True
        print("Nombre del usuario inválido. Solo debe contener letras (A-Z, a-z).")
        return False

    def validar_nombre_video(self):
        #Valor alfanumérico (A-Z, a-z, 0-9 )
        if re.fullmatch(r"[A-Za-z0-9 ]+", self.elemento_para_validar):
            return True
        print("Nombre del video inválido. Debe ser alfanumérico (A-Z, a-z, 0-9).")
        return False

    def validar_extension_video(self):
        #Valor alfanumérico (A-Z, a-z, 0-9) seguido de .com
        if re.fullmatch(r"[A-Za-z0-9]+\.(com)", self.elemento_para_validar):
            return True
        print("Extensión del video inválida. Debe ser alfanumérica seguida de '.com'.")
        return False

    def validar_tamaño(self):
        #Valor numérico (0-3)
        if self.elemento_para_validar <= 3:
            return True
        print("Tamaño inválido. Debe ser un número entre 0 y 3.")
        return False

def index(request):
    mensajeParaID = False
    mensajeParaNombre = False
    
    if request.method == "POST":
        #Obtener los datos del formulario
        usuario_id = request.POST.get("usuarioID")
        usuario_nombre = request.POST.get("usuarioNombre")
        if Validaciones(usuario_id).validar_usuario_id() == False:
            mensajeParaID = True
        if Validaciones(usuario_nombre).validar_nombre_usuario() == False:
            mensajeParaNombre = True

        #Si hay algún error de validación, renderiza con los mensajes de error
        if mensajeParaID or mensajeParaNombre:
            return render(request, "index.html", {
                "mensajeParaID": mensajeParaID,
                "mensajeParaNombre": mensajeParaNombre
            })

        #Crear o recuperar el usuario desde la base de datos
        usuario, existe = Usuario.objects.get_or_create(usuarioID=usuario_id, usuarioNombre=usuario_nombre)
        
        #Redirigir a la interfaz de usuario con el ID del usuario
        return redirect('interfazUsuario', user=usuario)
    
    return render(request, "index.html", {"mensajeParaID": mensajeParaID, "mensajeParaNombre": mensajeParaNombre})

def interfazUsuario(request, user):
    #Recuperar el usuario por su ID
    usuario = Usuario.objects.get(usuarioID=user)
    
    #Obtener los videos de ese usuario
    videos = Video.objects.filter(usuario=usuario)
    
    mensajeNombreVideo = False
    mensajeRutaVideo = False
    mensajeTamañoVideo = False
    
    if request.method == "POST":
        nombreVideo = request.POST.get("nombreVideo")
        rutaVideo = request.POST.get("rutaVideo")
        tamañoVideo = float(request.POST.get("videoTamaño"))
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
        #Validamos que todos los campos requeridos están completos
        #tamañoVideo = float(tamañoVideo)  # Convertimos a float si tiene valor válido
        #Crea y guarda el nuevo video en la base de datos
        nuevo_video = Video(
                videoNombre=nombreVideo,
                videoRuta=rutaVideo,
                videoTamaño=tamañoVideo,
                usuario=usuario  #Aquí estamos usando el objeto `usuario` recuperado
                )
        nuevo_video.save()
        return render(request, "interfazDeUsuario.html", {
                "videos": videos,   
            })
    #Renderizamos el HTML completo con el mensaje y los videos filtrados
    return render(request, "interfazDeUsuario.html", {
                "videos": videos,  
            })

def allVideos(request):
    videos = Video.objects.all()
    return render(request,"videos.html",{'videos':videos})

def eliminarVideo(request,NombreDelVideo):
    video = Video.objects.get(videoNombre=NombreDelVideo)
    usuario = video.usuario #extraemos el id del usuario de la variable video
    #print(usuario)
    video.delete()
    return redirect('interfazUsuario', user=usuario)