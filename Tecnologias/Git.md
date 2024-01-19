# Que es Git

Es un sistema de control de versiones distribuido gratuito y de codigo abierto diseñado para manejar todo, desde proyectos pequeños hasta proyectos muy grandes, con rapidez y eficiencia.

Git es un arbol donde se encuentra tu aplicacion en produccion y cada rama del tronco seran versiones distintas del sistema.En estas ramas puedes realizar cambios, pruebas con tal de asegurar el correcto funcionamiento. A continuacion implementarlo a la rama principal.

Github es un sitio web donde almacenamos nuestros proyectos, con la capacidad de clonar nuestros repositorios desde cualquier parte del mundo.

# Comandos basicos de la terminal

|Comando|Accion|
|-|-|
|ls|despliega las carpetas|
|cd nameCarpeta|ingresa a la carpeta|
|touch archivo.extension|crea un archivo|
|mkdir nombre| crea la carpeta|
|cat > archivo.extension| Modifica el archivo|
| rm -rf nombre.extension|borra el archivo|



# Configuracion de git

Para configurar git es necesario descargarlo desde la pagina oficial https://git-scm.com/downloads

A continuacion es importante ejecutar el siguiente comando en los terminal
> git config --global user.name "nombre"

> git config --global user.email "email@gmail.com"

# Inicializar un proyecto con Git

Es importante desde la terminal pre seleccionar la ruta donde se encuentra nuestro proyecto de software, una vez ahi. Ejecutamos el siguiente comando:

> git init

si el repositorio es remoto es necesario ejecutar el siguiente comando:

> git remote add origin "url"

esto vinculara ambos repositorios, para traer los cambios es necesario usar

> git pull origin main


# Renombrar ramas

Por default la rama principal de git es llamada master, sin embargo es posible cambiar el nombre de esta rama a main. Para ello ejecutamos el siguiente comando:

> git branch -m main

# Comprobar estado

Si quieres saber si algunos archivos en su ultima version se encuentran dentro de tu  ultima actualizacion de tu proyecto es necesario ejecutar:

> git status

# Agregar archivos a la zona de intercambio temporal

Para agregar archivos a tu proyecto es necesario ejecutar el siguiente comando:

> git add .

El anterior agregara todos los archivos que se encuentren dentro de tu proyecto. Si deseas agregar un archivo en especifico es necesario ejecutar el siguiente comando:

> git add nameFile.extension

# Eliminar archivos de la zona de intercambio temporal

Para eliminar archivos de la zona de intercambio temporal es necesario ejecutar el siguiente comando:

> git reset 


# Crear commit

Para crear un commit es necesario ejecutar el siguiente comando:

> git commit -m "NEW::"

en caso no especifiques el mensaje de tu commit, git abrira un editor de texto para que puedas escribirlo. En este comentario es importante especificar los cambios realizados en el proyecto.

para moverse entre commits es necesario ejecutar el siguiente comando:

> git checkout "nombre_del_commit"

para editar un commit es necesario ejecutar el siguiente comando:

> git commit --amend -m "NEW::"

# Historial de commit

Para ver el historial de commit es necesario ejecutar el siguiente comando:

> git log

mostrara las ramas de manera grafica

> git log --graph

si quieres ver quien ha hecho cambios en un fichero en particular es necesario ejecutar el siguiente comando:

> git annotate nombre.extension


# Volver para atras 

Si deseas volver a un commit anterior es necesario ejecutar el siguiente comando:

> git checkout "nombre_del_archivo.extension"



# Crear una variable que almacena un comando

Para crear una variable que almacene un comando es necesario ejecutar el siguiente comando:

> git config --global alias.nameVariable "comando"

para llamarlo se ejecuta el siguiente comando:

> git nameVariable


# Ignorar archivos

Para ignorar archivos es necesario crear un archivo llamado .gitignore y dentro de este colocar los archivos que deseas ignorar. Este archivo debe crearse en la raiz del proyecto. Para ello ejecutamos el siguiente comando:

> touch .gitignore

```
**/nombre_del_archivo
```

# Comparar cambios entre commits 

Para comparar cambios entre commits es necesario ejecutar el siguiente comando:

> git diff 

otro comando a utilizar puede ser

> git show


# Mover la cabecera del proyecto 

Al mover la cabecera de tu proyecto en la rama implica que los cambios efectuados (commits) despues de el commit actual donde te encuentres seran borrados. Para ello es necesario ejecutar el siguiente comando:

> git reset --hard "nombre_del_commit"


# Recuperar archivos eliminados por un reset

Para recuperar archivos eliminados por un reset es necesario ejecutar el siguiente comando:

> git reflog

este comando sirve para ver el historial de commits, asi poder hallar una version anterior del archivo eliminado

luego ejecutaremos de nuevo el reset a la id del commit donde se encontraba el archivo eliminado

> git reset --hard "id_del_commit"

# Crear un tag 

Un tag es un conjunto de commit que conforman la version de un proyecto. Para crear un tag es necesario ejecutar el siguiente comando:

> git tag "nombre"

para enlistar los tags es necesario ejecutar el siguiente comando:

> git tag

# Ramas    

Para crear una rama es necesario ejecutar el siguiente comando:

> git branch "nombre"

para moverme entre ramas es necesario ejecutar el siguiente comando:

> git switch "nombre"

para traer el contenido de tu rama remoto a local

> git pull origin nombre_de_la_rama

para mandar tus ramas de local a remoto 

> git push origin nombre_de_la_rama

Para combinar ramas es necesario ejecutar el siguiente comando:

> git merge "nombre"

eliminar una rama

> git branch -d "nombre"

# Volver a versiones anteriores de un archivo

La siguiente linea volvera a la ultima version guardada del archivo

> git checkout -- indice.txt

de una forma mas gener  al 

> git checkout -- .

# Almacenar cambios temporales

Para almacenar cambios temporales es necesario ejecutar el siguiente comando:

> git stash

para ver los cambios guardados

> git stash list

para volver a los cambios guardados

> git stash pop

para elimianr los cambios guardados

> git stash drop

# Conflictos

Si existen archivos en conflicto es bueno ejecutar un git fetch con el proposito de descargar los cambios sin que tus archivos se vean modificados

> git fetch


# GitHub

# Clonar proyectos

si deseas traer un repositorio ajeno a tu proyecto es necesario ejecutar el siguiente comando:

> git fork "url"



# GitLab

# Crear un nuevo proyecto (repositorio)

Desde la pagina principal de gitlab nos dirigimos al apartado de "New Project".

![](imagenes/newproyect.png)

A continuacion seleccionamos proyecto en blanco

![](imagenes/blankproject.png)

![](imagenes/crearapp.png)

# Clonar un proyecto

Nos dirigimos al proyecto dentro de la plataforma y seleccionamos la ruta https


![](imagenes/cloneone.png)

![](imagenes/clonetwo.png)

Ahora nos dirijimos a un directorio dentro de nuestro sistema operativo y seleccionamos abrir con git bash 

![](imagenes/opengitbashere.png)

Dentro de la terminal copiamos el siguiente comando

> git clone https://RutaCopiadaArriba

![](imagenes/gitclone.png)

La anterior accion abrira un nuevo menu de GitLab donde debemos loguear nuestra cuenta en la cual se encuentra el repositorio

![](imagenes/logingitlab.png)

En el navegador damos autorizacion y ya se nos abra clonado nuestro repositorio

![](imagenes/clonesuccesfull.png)

IMPORTANTE → Configurar un usuario global utilizando los siguientes comandos 

> git config --global user.email "juanromero2719@gmail.com"

> git config --global user.name "Sebastian R"

# Crear ramas

vamos a la consola de gitBash y colocamos el siguiente comando 

> git checkout -b nameBranch

esto creara una nueva rama y los dirije automaticamente a ella. 

Para actualizar la rama en la aplicacion realizamos el siguiente comando

> git push -f origin test:test

Para crear rama de desarrollo

> git checkout -b nombre_de_la_rama

para mandar tus ramas de local a remoto 

> git push origin nombre_de_la_rama



# Comandos

|Comando|Accion|
|-|-|
|ls|despliega las carpetas|
|cd nameCarpeta|ingresa a la carpeta|
|git branch|vemos las ramas|
|git status|ver si hay cambios|
|git checkout nameRama| cambia a la rama|
|git pull origin main|trae todos los cambios de main|
|vi name.extension| crea archivos|
|esc, wq|para salir y guardar|
| git status -u|presenta todo el contenido|
|rm -rf name.extension|borra el archivo|
|mkdir| crea la carpeta|
|git add .| agrega todos los cambios|
|git commit -m "NEW::"| acepta los cambios hechos dentros del repo|
|git log| ver los commit|


# Merge request

comanzamos empujando todos los cambios realizados a una nueva rama

> git push -f origin dev1:dev1

mech request -> especifica el cambio que se esta realizando al proyecto

para crear un merge request nos dirigimos al sidebar, en pinned y seleccionamos merge request.

![](imagenes/sidebarmerge.png)

es muy importante no mandar los cambios directamente hacia la rama de main sin antes haber pasado por la rama de test

![](imagenes/devtotest.png)

Dentro de la seccion de comparar branches es necesario dar una clara descripcion de los cambios realizados ademas de posibles configuraciones y dependencias necesarias.

Especificar la persona la cual hizo los cambios y la persona que revisara estos cambios.

![](imagenes/detallesmerge.png)

Una vez comprobados los cambios al momento de realizar la migracion a main se importante especificar en la descripcion usando el simbolo de "!" el branch que se esta subiendo 

![](imagenes/testtomain.png)