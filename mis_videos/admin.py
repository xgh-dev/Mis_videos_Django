from django.contrib import admin
from .models import Usuario,Video #aqui importamos los modelos

# Register your models here.
#haremos que las bases de datos se puedan modificar con el sitio administrativo
admin.site.register(Usuario)
admin.site.register(Video)
