# Ejemplo de una aplicación de App Engine compuesta por dos microservicios

En este ejemplo se muestra una aplicación compuesta por dos microservicios (default y backend). La aplicación se despliega en App Engine dentro de [Google Cloud Platform](https://cloud.google.com/). 


## 1. Pre-requisitos

* Tener una cuenta activa en [Google Cloud Platform](https://cloud.google.com/).
* Tener instalado el [Google Cloud SDK](https://cloud.google.com/sdk/).
* Acceso a Internet.


## 2. Estructura del proyecto

A continuación se describen los archivos y carpetas que forman parte del proyecto, así como la función que juega cada uno de ellos:

### 2.1 Servicio principal

- [app.yaml](app.yaml): Archivo de configuración.
- [main.py](main.py): Código de la aplicación.
- [requirements.txt](requirements.txt): Archivo que contiene las dependencias.
- [services_config.py](services_config.py): Archivo de configuración de los servicios.

### 2.2 Servicio [backend](backend/)

- [backend/app.yaml](backend/app.yaml): Archivo de configuración.
- [backend/main.py](backend/main.py): Código de la aplicación.
- [backend/requirements.txt](backend/requirements.txt): Archivo que contiene las dependencias.


## 3. Instrucciones de uso

1. Descargue el repositorio a una carpeta de su computadora utilizando el comando `git clone`.
2. Cámbiese a la carpeta del proyecto.
3. Verifique que el servicio principal funciona localmente, creando un entorno virtual, instalando las dependencias y ejecutando el servidor de desarrollo:

`virtualenv env`

`source env/bin/activate`

`pip install -r requirements.txt`

`python main.py`

4. Abra otra Terminal y cámbiese a la carpeta `backend`. Verifique que el servicio `backend` funciona localmente, creando un entorno virtual, instalando las dependencias y ejecutando el servidor de desarrollo:

`virtualenv env`                                                       

`source env/bin/activate`

`pip install -r requirements.txt`

`python main.py`

5. Abra un navegador y acceda a las siguientes URLs:
- Servicio principal: [http://localhost:8080](http://localhost:8080) 
- Servicio backend: [http://localhost:8081](http://localhost:8081)

6. Si pudo acceder correctamente a cada servicio, termine la ejecución de los servidores de desarrollo oprimiendo la combinación `Ctrl + C` en cada Terminal.
7. Cree un proyecto en la [Consola de Google Cloud Platform](https://console.cloud.google.com). Póngale el nombre y ID que usted prefiera.
8. Inicie sesión en su cuenta de GCP desde su terminal:

`gcloud auth login`

9. Active su proyecto:

`gcloud config set project PROJECT_ID`

10. Despliegue la aplicación en App Engine:

`gcloud app deploy app.yaml backend/back.yaml`

11. Acceda a la aplicación mediante la URL mostrada como resultado del paso anterior o el comando:

`gcloud app browse`

## Opcional (Configurar Cloud Endpoints)

A continuación se muestran los pasoa a seguir para habilitar la autenticación de la API y el control de la misma utilizando [Google Cloud Endpoints](https://cloud.google.com/endpoints).

0. Antes de realizar cualquier operación, modifique los archivos `openapi.yaml` y `app-endpoints.yaml` y sustituya PROJECT_ID por el ID de su proyecto.

1. Despliegue el servicio de Cloud Endpoints utilizando el comando:

`gcloud endpoints services deploy swagger.yaml`

2. Consulte los servicios habilitados:

`gcloud services list`

3. Verifique que en la salida aparecen los siguientes servicios requeridos:

| Name                             | Title                  |
|----------------------------------|------------------------|
| servicemanagement.googleapis.com | Service Management API |
| servicecontrol.googleapis.com    | Service Control API    |
| endpoints.googleapis.com         | Google Cloud Endpoints |

4. En caso de no aparecer algún servicio, habilítelo con el comando:

`gcloud services enable  SERVICE_NAME`

por ejemplo:

`gcloud services enable  endpoints.googleapis.com`

5. Despliegue la aplicación con la configuración que incluye Cloud Endpoints:

`gcloud app deploy app-endpoints.yaml backend/back.yaml`

6. Genere una API key siguiendo las instrucciones que aparecen [aquí](https://cloud.google.com/docs/authentication/api-keys#creating_an_api_key).

7. Habilite su API siguiendo estas [instrucciones](https://cloud.google.com/endpoints/docs/openapi/enable-api).


## 4. Recursos

Para conocer más sobre App Engine consulte la documentación oficial disponible en  [Google App Engine](https://cloud.google.com/appengine/).

Para conocer más sobre los microservicios en App Engine consulte la documentación oficial disponible en  [Microservices Architecture on Google App Engine](https://cloud.google.com/appengine/docs/standard/python/microservices-on-app-engine).

Para aprender a trabajar con el comando `gcloud` consulte la documentación oficial disponible en [gcloud command-line tool overview](
https://cloud.google.com/sdk/gcloud/).

Para conocer más sobre Google Cloud Platform consulte la documentación oficial disponible en  [GCP Documentation](https://cloud.google.com/docs/).
