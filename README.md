# Instrucciones para configurar entorno:

	El CRUD está construido usado Django, Python3 y Sqlite3.
	
	Ejecutar lo siguientes comandos para instalar las dependencias necesarias:

`pip install -r requirements.txt`

## Migraciones:

	En caso de utilizar una version de python3 ejecutar los siguientes comando:

##### Crear migraciones:
`python3 manage.py makemigrations`
#####  Ejecutar migraciones:
`python3 manage.py migrate`

> **Si utilizo una versión inferior a python3, remplazar `python3` por `python`, ejemplo: `python manage.py makemigrations`**


## Base de Datos:
Configuración `/settings.py` :
	
	'ENGINE': 'django.db.backends.sqlite3', 
	'NAME': 'crud_django.db', #nombre de la base de datos
	
	
## Crear usuario administrador de Django
Para acceder y administrar la interfaz de administrador, ejecute el siguiente comando:

Sugerencia: para esta instalación local use al usuario como admin y la contraseña como admin.

`python3 manage.py createsuperuser`
- Username (leave blank to use 'user'): admin
- Email address: your-user@mail.com
- Password: admin
- Password (again): admin

## Ejecute la aplicación web Django

Ejecutar aplicación con el siguiente comando:

`python3 manage.py runserver`
