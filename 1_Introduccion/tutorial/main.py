from flask import Flask
from flask import render_template

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


if __name__ == '__main__':
	# Ejecutamos el método run de la instancia app
	# Podemos indicar el puerto de escucha
	# Es recomendable poner en True parámetro debug para indicarle al servidor que estamos en la fase de desarrollo
	app.run(debug = True, port = 9000)