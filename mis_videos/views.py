#para hacer consulta usamos import psycopg2 y definimos las conexiones y el cursor para proceder a desarrollar las consultas
# Create your views here.
import re
#from django.http import HttpResponse
from .models import Video,Usuario
from django.shortcuts import render,redirect
# redirect dirige el usuario a otra URL y se utiliza el request de la vista en la cual se ejecuta, redirige al usuario a otra URL o vista, como si se hiciera una nueva solicitud.
# render, renderiza una plantilla y la muestra en la misma solicitud
#Usa render cuando quieras presentar una página directamente, y redirect cuando sea necesario redirigir al usuario a otro lugar

#from validaciones import validar_usuario_id,validar_nombre_usuario,validar_nombre_video,validar_tamaño,validar_extension_video


def validar_usuario_id(numero_nomina):
    # Valor alfanumérico (A-Z, a-z, 0-9)
    if re.fullmatch(r"[A-Za-z0-9]+", numero_nomina):
        return True
    print("Número de nómina inválido. Debe ser alfanumérico (A-Z, a-z, 0-9).")
    return False

def validar_nombre_usuario(nombre_usuario):
    # Valor alfabético (A-Z, a-z)
    if re.fullmatch(r"[A-Za-z]+", nombre_usuario):
        return True
    print("Nombre del usuario inválido. Solo debe contener letras (A-Z, a-z).")
    return False

def validar_nombre_video(nombre_video):
    # Valor alfanumérico (A-Z, a-z, 0-9 )
    if re.fullmatch(r"[A-Za-z0-9 ]+", nombre_video):
        return True
    print("Nombre del video inválido. Debe ser alfanumérico (A-Z, a-z, 0-9).")
    return False

def validar_extension_video(extension_video):
    # Valor alfanumérico (A-Z, a-z, 0-9) seguido de .com
    if re.fullmatch(r"[A-Za-z0-9]+\.(com)", extension_video):
        return True
    print("Extensión del video inválida. Debe ser alfanumérica seguida de '.com'.")
    return False

def validar_tamaño(tamano):
    # Valor numérico (0-3)
    if re.fullmatch(r"[0-3]", tamano):
        return True
    print("Tamaño inválido. Debe ser un número entre 0 y 3.")
    return False


def index(request):
    mensajeParaID = False
    mensajeParaNombre = False
    
    if request.method == "POST":
        # Obtener los datos del formulario
        usuario_id = request.POST.get("usuarioID")
        usuario_nombre = request.POST.get("usuarioNombre")
        if validar_usuario_id(usuario_id) == False:
            mensajeParaID = True
        if validar_nombre_usuario(usuario_nombre) == False:
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
        if validar_nombre_video(nombreVideo) == False:
            mensajeNombreVideo = True
        if validar_extension_video(rutaVideo) == False:
            mensajeRutaVideo = True
        if validar_tamaño(tamañoVideo) == False:
            mensajeTamañoVideo = True
        if mensajeNombreVideo or mensajeRutaVideo or mensajeTamañoVideo:
            return render(request, "interfazDeUsuario.html", {
                "videos": videos, 
                "mensajeNombreVideo": mensajeNombreVideo,
                "mensajeRutaVideo": mensajeRutaVideo,
                "mensajeTamañoVideo": mensajeTamañoVideo,   
            })
        # Validamos que todos los campos requeridos están completos
        tamañoVideo = float(tamañoVideo)  # Convertimos a float si tiene valor válido
        # Crea y guarda el nuevo video en la base de datos
        nuevo_video = Video(
                videoNombre=nombreVideo,
                videoRuta=rutaVideo,
                videoTamaño=tamañoVideo,
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
    videos = Video.objects.all()
    return render(request,"videos.html",{'videos':videos})

def eliminarVideo(request,NombreDelVideo):
    video = Video.objects.get(videoNombre=NombreDelVideo)
    usuario = video.usuario
    video.delete()
    return redirect('interfazUsuario', user=usuario.usuarioID)