#from django.shortcuts import render
# Create your views here.
import re
from django.http import HttpResponse
from .models import Video,Usuario
from django.shortcuts import render,redirect
#from validaciones.validaciones import validar_nombre_usuario,validar_usuario_id
#
def validar_usuario_id(numero_nomina):
    # Valor alfanumérico (A-Z, a-z, 0-9)
    if re.fullmatch(r"[A-Za-z0-9]+", numero_nomina):
        return True
    print("Número de nómina inválido. Debe ser alfanumérico (A-Z, a-z, 0-9).")
    return False
#
def validar_nombre_usuario(nombre_usuario):
    # Valor alfabético (A-Z, a-z)
    if re.fullmatch(r"[A-Za-z]+", nombre_usuario):
        return True
    print("Nombre del usuario inválido. Solo debe contener letras (A-Z, a-z).")
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
    
    mensaje = False  # Variable para mensajes de confirmación o error
    
    if request.method == "POST":
        nombreVideo = request.POST.get("nombreVideo")
        rutaVideo = request.POST.get("rutaVideo")
        tamañoVideo = request.POST.get("videoTamaño")
        
        # Validamos que todos los campos requeridos están completos
        if nombreVideo and rutaVideo and tamañoVideo:
            try:
                tamañoVideo = float(tamañoVideo)  # Convertimos a float si tiene valor válido
                # Crea y guarda el nuevo video en la base de datos
                nuevo_video = Video(
                    videoNombre=nombreVideo,
                    videoRuta=rutaVideo,
                    videoTamaño=tamañoVideo,
                    usuario=usuario  # Aquí estamos usando el objeto `usuario` recuperado
                )
                nuevo_video.save()
                mensaje = "El video se guardó correctamente."
                return render(request, "interfazDeUsuario.html", {"videos": videos, "mensaje": mensaje})
            except ValueError:
                mensaje = True
        else:
            mensaje = True
    
    # Renderizamos el HTML completo con el mensaje y los videos filtrados
    return render(request, "interfazDeUsuario.html", {"videos": videos, "mensaje": mensaje})

def allVideos(request):
    videos = Video.objects.all()
    return render(request,"videos.html",{'videos':videos})

def eliminarVideo(request,NombreDelVideo):
    video = Video.objects.get(videoNombre=NombreDelVideo)
    usuario = video.usuario
    video.delete()
    return redirect('interfazUsuario', user=usuario.usuarioID)