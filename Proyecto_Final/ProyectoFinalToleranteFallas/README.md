# Proyecto - Computación Tolerante a Fallas 
En este repositorio se encuentra el proyecto final para la materia Computacion tolerante a fallas Profesor: Michel Emanuel Lopez Franco.

![Aplicacion web que genera contraseñas](./images/app.PNG)


## Descripción
La aplicacion es un generador de contraseñas, el usuario ingresa el tamaños de a cadena de caracteres, señala si puede incluir Mayúsculas, Minúsculas, Números y Símbolos

La aplicación fue 3laborada con:
    -HTML
    -CSS
    -JavaScript

Tecnologias para el despliegue de la aplicación: 
    -Docker 
    -OpenShift
    
### Docker
Descargamos e instalamos Docker en el equipo:
https://www.docker.com/products/docker-desktop/
Seleccionamos el tipo de sistema operativo, una vez terminada la instalación nos pedirá reiniciar el equipo.
Abrimos CMD y comprobamos la instalación con: ``` docker versión ``` o ```docker –version```

Creamos un archivo ‘Dockerfile’ (un archivo Docker que tendrá las instrucciones necesarias para crear el entorno)

![dockerfile](./images/dockerfile.PNG)

Una vez que tu código esté listo y el Dockerfile está escrito, todo lo que tienes que hacer es crear tu imagen para contener tu aplicación: docker build -t "nombre:tag"

En nuestro caso: docker build -t password-generator:v1

![construccion](./images/dockerbuild.PNG)

Mostramos las imagenes de docker con: docker images

![imagenes](./images/lookimages.PNG)

Creada la imagen realizamos el lanzamiento: docker run -d -p 80:80 password-generator:v1

![despliegue](./images/port8080.PNG)

En Docker desktop podemos realizar el despliegue de la siguiente manera:
1. Seleccionamos la imagen creada y la corremos

![imgaendesktop](./images/runningdocker.PNG)

2. Seleccionamos el contenedor con la imagen de que creamos y damos click en el puerto 80:80

![contenedordesktop](./images/runningdocker.PNG)

Se habre el navegador web por defecto y nos aparece la aplicacion:

![aplicacion](./images/openshiftcreate.PNG)

### ⭕🖥 OpenShift 🖥⭕
Ingresamos a la página web de RedHat, creamos un perfil e ingresamos para usar DevSandBox.
https://developers.redhat.com/developer-sandbox

Una vez dentro del DevSandBox, nos posicionamos en la navegación como “Developer”.

![inicio sandbox](./images/inicio sandbox.png)
 
Una vez en la posicionados en la vista de “Developer” nos dirigimos a la sección de “Add” para agregar nuestra app que en esta ocasión será mediante la opción de “Git Repository”.

![sección add](./images/addgithub.PNG)
 
En esta pestaña añadimos la URL de nuestro repositorio de GitHub y así procedemos a crear nuestra app en OpenShift.

![importar git 1](./images/openshift1.PNG)

![importar git 2](./images/openshift2.PNG)

Ahora en la sección de “Topology” podemos ver que el deploy de nuestra app está listo y en ejecución.

![sección topology](./images/topology.PNG)
 
Finalmente abrimos en otra pestaña nuestra app para comprobar que todo funciona de manera satisfactoria.
 
 ![deploy openshfit](./images/localhost.PNG)
