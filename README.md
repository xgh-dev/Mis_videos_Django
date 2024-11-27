PROYECTO MIS VIDEOS

Mediante este entregable, culmino mi certificación de fullstack. Quiero mencionar que fueron unos 10 meses muy agradables e interesantes por que estuve aprendiendo de todo un poco y pude seleccionar las tecnologias que mas me llamaron la atención. La idea de este documento es hablar un poco a detalle de este proyecto para dar una orientación respecto a su funcionamiento.

Este proyecto cuanta con 3 vistas que se renderizan. La vista principal es la vista donde tendremos nuestro login, esta vista se encarga de dos cosas de recibir datos de usuario para crear un registro de este e iniciar sesión y llevarnos a la interfaz de usuario o de lo contrario en caso de que este exista nos llevara a la interfaz mencionada, la segunda función que tiene es llevarnos a una vista que renderiza todos los viedeos guardados en la base de datos para ver lo que se tiene registrado sin importar el usuario con el que se registro.

Hablando con mas detalle de la vista de interfaz de usuario, esta vista se encarga de renderizar una lista de los videos que el usuario guarde, de igual menera esta lista renderiza un boton que se encarga de eliminar el video seleccionado y tambiens se muestra el formulario que recibe datos por parte del usuario para guardar nuevos videos. Estos datos al igual que los datos que se ingresan en el login son sometidos a validaciones, en caso de alguna validación encuentre un caracter que no este permitido en su campo, se mostrara una alerta que pide al usuario corregir esa captura de datoos para que no se encuentre algun error.

Con esta introducción podemos dar paso a los detalles tecnicos de la aplicación.

Esta aplicación esta construida en el framework Django, este framework esta desarrollado con python y trabaja con este lenguage, este framework nos permite crear proyectos web estaticos con mucha facilidad siempre y cuando nos acerquemos a leer la documentación de este framewrok. 
Para poder ejecutar la aplicación se deben considerar algunos detalles para este, principalmente en la cuestion de activar el entorno virtual que contiene las dependencias y librerias utilizadas para la ejecución de la aplicación y el cambio de datos en el archivo settings de la carpeta mysite.

Una vez activado el entorno virtual mediante los siguentes comandos .\env\Scripts\Activate ejecutaremos el servidor con este comando python manage.py runserver, una vez hecho esto deberemos cambiar los datos de la base de datos en el archivo settins a la base de datos que estaremos usando, en este caso se trabaja con una base de datos de tipo postgreSQL y en caso de que se quiera utilizar otro tipo de base de datos se tiene que modificar el concepto de ENGINE del objeto DATABASES en el archivo settings de igual manera que los campos de acceso a la base de datos.

Finalmente podremos ejecutar nuestra aplicación y quien quiera podra tener acceso. Agradezco su atencion y espero el proyecto sea del agrado del usuario.