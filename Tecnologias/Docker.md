# Que es un contenedor?

Un contenedor es una unidad de software estandarizada que empaqueta el codigo y todas sus dependencias para que la aplicacion se ejecute de forma rapida y confiable desde un entorno de computacion a otro.

# Que es docker

Es una maquina virtual ligera que permite empaquetar aplicaciones y sus dependencias en contenedores aislados, que pueden ejecutarse en cualquier servidor. 

# Que es una imagen de docker

Es un paquete de software ligero, independiente y ejecutable que incluye todo lo necesario para ejecutar una aplicacion: codigo, tiempo de ejecucion, herramientas del sistema, bibliotecas del sistema y configuraciones.

# Descargar imagenes

Para descargar una imagen de docker se utiliza el comando `docker pull "nombre de la imagen"`

si deseas descargar una version en espefico de la imagen se utiliza el comando `docker pull "nombre de la imagen":"version"`

si deseas eliminar una imagen de docker se utiliza el comando `docker image rm "nombre de la imagen"`

# Crear contenedores

para crear un contenedor se utiliza el comando `docker create "nombre de la imagen"`

tambien podemos asignarle un nombre al contenedor con el comando `docker create --name "nombre del contenedor" "nombre de la imagen"`

si es necesario asignarle un puerto al contenedor se utiliza el comando `docker create  -p"puerto de nuestra maquina":"puerto del contenedor" --name "nombre del contenedor" "nombre de la imagen"`

este comando crea un contenedor pero no lo ejecuta, es necesario copiar el id del contenedor y ejecutarlo con el comando `docker start "id del contenedor"`

para verificar que el contenedor corre de manera correcta se utiliza el comando `docker ps`

para detener un contenedor se utiliza el comando `docker stop "id del contenedor"`

para eliminar un contenedor se utiliza el comando `docker rm "id del contenedor"`

o tambien puede ser eliminado utilizando el nombre del contenedor `docker rm "nombre del contenedor"`

# Resumen

Docker run
* Descarga una imagen de docker (si no existe) 
* crear un contenedor 
* Inicia un contenedor 

`docker run "nombre de la imagen"` si no quieres ver los logs automatica se crea el contenedor utilizamos el comando `docker run -d "nombre de la imagen"`

# Historial

para poder ver el historial de los comandos que hemos utilizado se utiliza el comando `docker logs "nombre de la imagen"`

# Como guardar los cambios de un contenedor

Dentro de la carpeta de nuestro proyecto crearemos un archivo llamado `Dockerfile` y dentro de este archivo escribiremos los comandos que queremos que se ejecuten al momento de crear el contenedor.

# Comandos de dockerfile

* FROM: Especifica la imagen base que se utilizara para crear la nueva imagen

> FROM "nombre de la imagen":version

a continuacion indicamos en que carpeta se guardara el archivo que se descargara

> RUN mkdir -p /home/app

a continuacion indicamos en que carpeta se guardara el archivo que se descargara

> COPY . /home/app

a continuacion indicamos el puerto que utilizara el contenedor

> EXPOSE 3000

a continuacion indicamos el comando que se ejecutara al momento de crear el contenedor

> CMD ["node", "/home/app/index.js"]

# Agrupar contenedores

para ver redes de docker se utiliza el comando `docker network ls`

para crear una red de docker se utiliza el comando `docker network create "nombre de la red"`

**una vez creada la red es importante recordar que la ruta para acceder a la base de datos cambiara, en lugar de utilizar localhost se utilizara el nombre de la red**

para crear una build de docker se utiliza el comando `docker build -t "nombre de la app":version .`

ahora para crear un contenedor de la app se utiliza el comando `docker create -p"puerto":"puerto" --name "nombre del contenedor" --network "nombre de la red" -e "variable de entorno"="valor" "nombre de la imagen:"

# Docker compose

Por cada contenedor 

* Descargar imagen
* Crear una red
* Crear contenedores
* Iniciar contenedores
    * Asignar puertos
    * % nombre
    * % variables de entorno
    * especificar red
    * indicar imagen:etiqueta

para automatizar este proceso se utiliza docker compose

para empezar se crea un archvio llamado `docker-compose.yml` y dentro de este archivo se escriben los comandos que se utilizaran para crear los contenedores

para empezar se debe indicar la version con la que se trabajara
```yaml
version: "3.9"
```
a continuacion se indica el nombre del servicio\


```yaml
services:
    nombre del contenedor:
        build: .
        ports:
            - "puerto de la maquina:puerto del contenedor"
        links:
            - nombre del contenedor
    nombre del contenedor
        image: "nombre de la imagen"
        ports:
            - "puerto de la maquina:puerto del contenedor"
        environment:
            - "nombre de la variable de entorno"="valor"
            - "nombre de la variable de entorno"="valor"
        volumes:
            - nombre del volumen/data/db
            - nombre del volumen/data/configdb
            # myqsl -> /var/lib/mysql
            # postgres -> /var/lib/postgresql/data

    
```

una vez definido el contenedor empleamos el comando `docker-compose up` para crear los contenedores

para eliminar los contenedores se utiliza el comando `docker-compose down`

para almacenar archivos en el tiempo, es importante definirlos aca abajo antes de crearlos arriba.

```yaml
volumes:
    nombre del volumen:
       
```
  

# Dockerizar un proyecto Django

Para empezar vamos a settings, y en la parte de `DEBUG` cambiamos su valor a false

ahora, en la parte de `ALLOWED_HOSTS` agregamos `'*'` para que cualquier host pueda acceder a nuestra app

configuramos nuestra base de datos en la seccion de `DATABASES`

```python
'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db_postgres',
        'PORT': 5432,
    
    }
```

ahora agregamos una linea de codigo al final del archivo

```python
STATIC_ROOT= '/code/static/'
```

creamos una carpeta en la raiz de nuestro proyecto llamada `config`

definimos un archivo llamado `requirements.txt` y dentro de este archivo escribimos las dependencias de nuestro proyecto

para ello mediante la consola ejecutaremos 

> pip freeze > requirements.txt

a continuacion crearemos 2 archivos mas, uno llamado `Dockerfile` y otro llamado `docker-compose.yml`

dentro de nuestro archivo Dockerfile escribiremos los comandos que se ejecutaran al momento de crear el contenedor

```dockerfile
FROM python:3.7

ENV PYTHONUNBUFFERED 1

RUN mkdir /code

WORKDIR /code
COPY . /code/

RUN pip install -r requirements.txt
```

a continuacion en nuestro archivo `docker-compose.yml` escribiremos los comandos que se ejecutaran al momento de crear el contenedor

```yaml
version: "3"

# Este servicio es el de la base de datos unicamente
services:
  db_postgres:
    image: postgres:11.5
    volumes:
      - ./postgres-data:/var/lib/postgresql/data

  django_app:
    build: .
    volumes:
      - static:/code/static
      - .:/code
    depends_on:
      - db_postgres 

volumes:
  .:
  postgres-data:
```

# Dockerizar un proyecto Django 2

* Paso 1: Crear un archivo llamado `Dockerfile`, crear un rachivo llamada `docker-compose.yml`, crear un archivo llamada `requirements.txt` y crear un archivo llamado `.env`
* Paso 2: Dentro del archivo `Dockerfile`
  * Definir la version a utilizar. Ej: `FROM python:3.7`
  * Definir la variable `ENV PYTHONUNBUFFERED 1`
  * Crear una carpeta llamada `code` Ej: `RUN mkdir /code`
  * Definir la carpeta de trabajo Ej: `WORKDIR /code`
  * Copiar el contenido de la carpeta actual a la carpeta de trabajo Ej: `COPY . /code`
  * Instalar las dependencias Ej: `RUN python -m pip install -r requirements.txt`
* Paso 3: Dentro del archivo `requirements.txt` definir las dependencias a utilizar Ej: `Dj
  * Django==3.1
  * django-environ==0.4.5
  * psycopg2-binary>=2.8
* Paso 4: Dentro del archivo `docker-compose.yml`
  * Definir la version a utilizar. Ej: `version: "3"
  * Definir los servicios. Ej:
    * ```yml 
      services:
        db:
          image: postgres:12
          env_file: .env

        web:
          build:
            context: .
          env_file: .env
          command: python manage.py runserver 0.0.0.0:8000
          volumes:
            - .:/code
          ports:
            - 8000:8000
          depends_on:
            - db
      ```
* Paso 5: Ejecutar el comando `docker-compose build`
* Paso 6: Ejecutar el comando `docker-compose up`
* Paso 7: Ejecutar el comando `docker-compose run web django-admin.py startproject nombre_proyecto .`
* Paso 8: En el archivo `Settings.py` agregamos el libreria environ. `import environ` 
* Paso 9: Copiar la SECRET_KEY y pegarla en el archivo .env retirando los espacios y las comillas
* Paso 10: en el archivo `Settings.py` pegar las siguientes lineas:
  * ```py
    # environt settings
    env = environ.Env() 
    ```
* Paso 11: Modificar la linea de SECRET_KEY por la siguiente:
  * ```py
    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = env('SECRET_KEY')
    ```
* Paso 12: Crear una nueva variable en el archivo .env. `DJANGO_DEBUG=True`
* Paso 13: Modificar la linea de DEBUG por la siguiente:
  * ```py
    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = env.bool('DJANGO_DEBUG', default=False)
    ```
* Paso 14: Crear nuevas variables en el archivo .env
  * ```
    ALLOWED_HOST=127.0.0.1,localhost
    POSTGRES_DB = my_database
    POSTGRES_USER = my_user
    POSTGRES_PASSWORD=my_password
    POSTGRES_HOST=db
    POSTGRES_PORT=5432
    ```
* Paso 15: Modificar la linea de ALLOWED_HOST por la siguiente 
  * ```py
    ALLOWED_HOSTS = tuple(env.list('ALLOWED_HOSTS', default=[]))
    ```
* Paso 16: Modificar la linea de DATABASE por la siguiente
  * ```py
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': env.str('POSTGRES_DB'),
            'USER': env.str('POSTGRES_USER'),
            'PASSWORD': env.str('POSTGRES_PASSWORD'),
            'HOST': env.str('POSTGRES_HOST'),
            'PORT': env.int('POSTGRES_PORT')
        }
    }
    ```
* Paso 17: Ejecutar el comando `docker-compose run web python manage.py migrate`
* Paso 18: Ejecutar el comando `docker-compose run web python manage.py createsuperuser`