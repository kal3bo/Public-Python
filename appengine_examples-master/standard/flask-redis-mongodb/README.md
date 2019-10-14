# Ejemplo de una aplicación compuesta por Flask + Redis + MongoDB utilizando App Engine

En este ejemplo se muestra una aplicación compuesta por una API desarrollada en [Flask](http://flask.pocoo.org/), una base de datos [Redis](https://redis.io/) para manejo de sesiones y una base de datos en [MongoDB](https://www.mongodb.com/) para el almacenamiento persistente de la información. La aplicación se despliega en App Engine dentro de [Google Cloud Platform](https://cloud.google.com/). 

Para Redis y MongoDB se utilizan servicios en la nube ofrecidos por [Redis Labs](https://redislabs.com/) y [mLab](https://mlab.com/) respectivamente.

## 1. Pre-requisitos

* Tener una cuenta activa en [Google Cloud Platform](https://cloud.google.com/).
* Tener una cuenta activa en Redis Labs o utilizar un servidor Redis local. Puede crear una cuenta gratuita [aquí](https://app.redislabs.com/#/sign-up/cloud).
* Tener una cuenta activa en [mLab](https://mlab.com/) o utilizar un servidor de MongoDB local. Puede crear una cuenta gratuita [aquí](https://mlab.com/signup/).
* Tener instalado el [Google Cloud SDK](https://cloud.google.com/sdk/).
* Acceso a Internet.


## 2. Estructura del proyecto

A continuación se describen los archivos y carpetas que forman parte del proyecto, así como la función que juega cada uno de ellos:

- [app.yaml](app.yaml): Archivo de configuración de la aplicación.
- [requirements.txt](requirements.txt): Archivo que contiene las dependencias de la aplicación.
- [config.py](config.py): Archivo de configuración de la aplicación.


## 3. Instrucciones de uso

1. Descargue el repositorio a una carpeta de su computadora utilizando el comando `git clone`.
2. Cámbiese a la carpeta del proyecto.
3. Verifique que el proyecto funciona localmente, creando un entorno virtual, instalando las dependencias y ejecutando el servidor de desarrollo:

`virtualenv env`   

`source env/bin/activate`

`pip install -r requirements.txt`

`python main.py`

3. Cree un proyecto en la [Consola de Google Cloud Platform](https://console.cloud.google.com). Póngale el nombre y ID que usted prefiera.
4. Inicie sesión en su cuenta de GCP desde su terminal:

`gcloud auth login`

5. Active su proyecto:

`gcloud config set project PROJECT_ID`

6. Despliegue la aplicación en App Engine:

`gcloud app deploy`

7. Acceda a la aplicación mediante la URL mostrada como resultado del paso anterior o el comando:

`gcloud app browse`


## 4. Recursos

Para conocer más sobre App Engine consulte la documentación oficial disponible en  [Google App Engine](https://cloud.google.com/appengine/).

Para aprender a trabajar con el comando `gcloud` consulte la documentación oficial disponible en [gcloud command-line tool overview](
https://cloud.google.com/sdk/gcloud/).

Para conocer más sobre Google Cloud Platform consulte la documentación oficial disponible en  [GCP Documentation](https://cloud.google.com/docs/).
