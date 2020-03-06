# Vamos a trabajar con la estructura modelo, vista controlador

# Nos vamos a apoyar de la clase Blueprint
# Esta clase nos permite trabajar con aplicaciones modulables
from flask import Blueprint
from flask import render_template

# Realizamos una instancia
# El primer argumento es el nombre de nuestro contexto
# El segundo argumento es el contexto del cual se está creando la instancia
page = Blueprint('page', __name__)

# Declaramos una función la cual se va a ejecutar en caso de que no se encuentre la página
# La función recibe un arguento, este es el error
# Por buenas prácticas regresamos dos valores
# El primer valor a regresar es lo que queremos retornar
# El segundo valor es un númoero o código que indique el tipo de error que se generó
@page.app_errorhandler(404)
def page_not_found(error):
	return render_template('errors/404.html'), 404

# Una vez creada esta instancia podemos crear la cantidad de rutas deseadas
@page.route('/')
def index():
# Podemos enviar un mensaje
#	return 'Hola mundo desde el archivo views'
# Podemos enviar un html
	return render_template('index.html', title='Index')
