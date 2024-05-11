# Guia para crear un proyecto en Python con Django


1) Tienen que tener Python instalado (estamos usando la 3.12)

    > Si usan pyenv, tienen que instalar la version de python que van a usar con el comando ```pyenv install 3.12```

2) Tienen que crear una carpeta en donde quieran tener el proyecto. Por ejemplo, pueden crear una carpeta ```backend``` en algun lado

3) Abrir la terminal en esa carpeta 

    > tambien pueden abrir el visual code en esa carpeta, y luego usar la terminal que tiene el mismo visual code

4) una vez que esten parados en esa carpeta, ejecutar el siguiente comando para crear el ```virtual env```:

    ```shell
    python -m venv ./venv
    ```

5) ya creado el virtual env, lo tienen que activar. eso se hace dependiendo de donde lo hagan:

    Si estan en windows (powershell o terminal):
    ```shell
    ./venv/Scripts/activate
    ```

    Si estan en macos o linux:
    ```shell
    source venv/bin/activate
    ```

6) una vez que ya creado y activado el virtual env, tenemos que instalar las dependencias de nuestro proyecto:

    ```shell
    pip install django
    pip install mysql-connector-python
    ```
    
7) ya con las dependencias instaladas, tenemos que crear la estructura de proyecto de django. Para eso ejecutamos el comando:

    ```shell
    django-admin startproject server .
    ```

    > Recordar agregar ese punto (".") al final. Este comando agrega la carpeta "server" al proyecto con todos los ficheros que son exclusivos de django y que en lo posible NO debemos tocar

8) creada la estructura de Django, podemos ejecutar el proyecto con el siguiente comando:

    ```shell
    python manage.py runserver
    ```

    > al hacer esto, el proyecto quedara constantemente ejecutandose, por lo que no hace falta que corramos este comando cada vez que hacemos cambios en el codigo


9) creamos una carpeta ```src``` en la raiz del proyecto (similar a como esta la estructura en este repositorio) donde pondremos todo nuestro codigo.

    Dentro de esa carpeta, crearemos las siguientes carpetas:

    - controllers: donde colocaremos los controladores que serviran de punto de entrada para las rutas

    - repositories: donde colocaremos los Repositorios, archivos que contienen funciones que ejecutan la conexion a la base de datos y traen datos

    - models: ahi colocaremos nuestras clases de dominio, nuestro modelo (clase Producto, Cliente, etc)

    - utils: colocaremos codigo de ayuda, como por ejemplo el Connector que usamos para conectarnos a la base de datos

10) dentro de la carpeta ```src``` creamos un archivo llamado ```urls.py``` donde pondremos nuestras rutas (ver ejemplo en este mismo repositorio)

11) hay que ir a la carpeta ```server``` (la que creó el Django) para modificar el ```urls.py``` y agregar un path para que incluya NUESTRO urls.py (ver ejemplo en este repositorio)

12) Listo, comenzar a programar. Recordar los siguientes tips:

    - Recuerden cambiar los datos de conexion de la base de datos en el archivo Connector
    - Acuerdensé el versito:

      > en urls.py se definen cuales van a ser las rutas de la API, y qué funcion debe ejecutarse cuando se accede a una ruta. Estas funciones corresponden a los CONTROLLERS que reciben la peticion y hacen algo. Normalmente lo que hacen es pedirle a un REPOSITORY datos de alguna entidad. Los repositorios usan el Connector para conectarse a la base de datos y obtener datos de las entidades. luego de llamar a la base de datos el repository crea MODELS con esos datos y es lo que retorna.

    - Recuerden que los controlers deben devolver JsonResponse SI O SI, por lo que deben crear el metodo ```serialize``` en cada una de las entidades (ver ejemplo en este mismo repositorio)

    - El que cree el proyecto, siga estos pasos. Los que clonen, tienen que hacer los pasos hasta el 6, solo que en vez de crear la carpeta, deben "clonarlo". RECORDAR QUE DEBEN PARARSE EN LA CARPETA QUE TENGA EL PROEYECTO, NO EN LA CARPETA "Proyecto 2024", sino no va a andar nada.

    