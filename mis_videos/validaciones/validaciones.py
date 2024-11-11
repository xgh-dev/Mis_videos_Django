import re

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

def validar_cantidad_videos(cantidad_videos):
    # Valor numérico (0-9)
    if re.fullmatch(r"[0-9]", cantidad_videos):
        return True
    print("Cantidad de videos inválida. Debe ser un número entre 0 y 9.")
    return False

def validar_titulo_video(titulo_video):
    # Valor alfanumérico (A-Z, a-z, 0-9)
    if re.fullmatch(r"[A-Za-z0-9]+", titulo_video):
        return True
    print("Título del video inválido. Debe ser alfanumérico (A-Z, a-z, 0-9).")
    return False

def validar_nombre_video(nombre_video):
    # Valor alfanumérico (A-Z, a-z, 0-9)
    if re.fullmatch(r"[A-Za-z0-9]+", nombre_video):
        return True
    print("Nombre del video inválido. Debe ser alfanumérico (A-Z, a-z, 0-9).")
    return False

def validar_extension_video(extension_video):
    # Valor alfanumérico (A-Z, a-z, 0-9)
    if re.fullmatch(r"[A-Za-z0-9]+", extension_video):
        return True
    print("Extensión del video inválida. Debe ser alfanumérica (A-Z, a-z, 0-9).")
    return False

def validar_tamaño(tamano):
    # Valor numérico (0-3)
    if re.fullmatch(r"[0-3]", tamano):
        return True
    print("Tamaño inválido. Debe ser un número entre 0 y 3.")
    return False
