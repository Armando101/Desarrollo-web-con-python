from flask import Flask
from flask import render_template, request

# Declaro una instancia de Flask y le paso como argumento el contexto
app = Flask(__name__)

# Para añadir recursos al servidor indicamos la ruta como argumento del método route que a su vez pertenece a la instancia
# Posteriormente declaramos la función
@app.route('/')
def index():
	name = "Armando"
	course = 'Python web'

	# Puedo poner condiciones que si son True se muestre una etiqueta en el archivo html {% if condition %} Etiqueta {% else %} Etiqueta {% endif %}
	is_premium = True

	# También puedo iterar con un for sobre una lista
	courses = ['Python', 'Ruby', 'Java', 'JavaScript']
	
	# Podemos regresar un archivo html
	# También puedo enviar argumentos al html
	# En el archivo html coloco entre dobles llaves el nombre del parámetro
	return render_template("index.html", username=name, course_name = course, is_premium=is_premium, courses=courses)

	# Podemos regresar algo sencillo como un mensaje
#	return "<h1>Hola mundo desde el servidor de Flask</h1>"

# Parámetros: podemos poner parámetros para evitar tener muchas urls
# Por defecto toma los parámetros como enteros pero podemos ponerlos de un tipo en específico, los parámetros también tendrán que ser especificados en la función
@app.route('/usuario/<username>/<int:age>')
def usuario(username, age):
	return 'Hola ' + username + " " +str(age)

# Podemos enviar datos al servidor con query strings
# Necesitamos el módulo request
# La variable args es un diccionario que recibe los datos que le mandamos desde la url
# Para enviar datos lo hacemos de la siguiente manera:
	# localhost:900/datos?nombre=Armando&curso=python_web
@app.route('/datos')
def datos():
	# Si le damos un string vacío indicamos que tome un valor por defecto
	nombre = request.args.get('nombre', '')
	curso = request.args.get('curso', '')
	return "Listado de datos: " + nombre + ", " + curso 


@app.route('/about')
def about():
	print('Estamos en el about')
	return render_template('about.html')

# Esta función es un callback
# Colocamos el siguiente decorador
@app.before_request
def before_request():
	# Esa función se ejecuta antes de resolver la petición
	# Nos permite hacer acciones como acceder a una base de datos, acceder a un servidor, etc.
	# Este print lo podemos ver en la consola
	print("Antes de la petición")

# Esta función será un callback que se ejecuta después de la petición
# La función recibe un argumento, este argumento es la respuesta de cada función ejecutada
@app.after_request
def after_reques(response):
	print('Después de la petición')
	return response


if __name__ == '__main__':
	# Ejecutamos el método run de la instancia app
	# Podemos indicar el puerto de escucha
	# Es recomendable poner en True pax|rámetro debug para indicarle al servidor que estamos en la fase de desarrollo
	app.run(debug = True, port = 9000)