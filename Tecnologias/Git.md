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

# Clonar proyectos

si deseas traer un repositorio ajeno a tu proyecto es necesario ejecutar el siguiente comando:

> git fork "url"

# Clonacion de un reposotorio GITLAB

* Paso 1: Ingresar a GitLab al Proyecto en cuestion y copiar la ruta del repositorio HTTPS
* Paso 2: Abrir la terminal de GitBash en la carpeta donde se desea clonar el repositorio
* Paso 3: Ejecutar el comando `git clone` y pegar la ruta del repositorio HTTPS
* Paso 4: Para agregar ramas adicionales es necesario crear nuevamente la rama con `git checkout -b nombre_de_la_rama`
* Paso 5: Para actualizar la rama en la aplicacion realizamos el siguiente comando `git pull origin nonbre_de_la_rama`



