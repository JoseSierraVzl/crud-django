# Instrucciones para configurar entorno:

	El CRUD está construido usado Django, Python3 y MySql, con las siguientes especificaciones:
	
- Python: 3.8.10
- Django: 4.1.7

## Migraciones:

	En caso de utilizar una version de python3 ejecutar los siguientes comando:

##### Crear migraciones:
`python3 manage.py makemigrations`
#####  Ejecutar migraciones:
`python3 manage.py migrate`

> **Si utilizo una versión inferior a python3, remplazar `python3` por `python`, ejemplo: `python manage.py makemigrations`**


## Base de Datos:
Configuración `/settings.py` :
	
	'ENGINE': 'django.db.backends.mysql', 
	'NAME': 'crud_django', #nombre de la base de datos
	'USER': '',
	'PASSWORD': '',
	'HOST': 'localhost'
	'PORT': '3306',
