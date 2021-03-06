# Vamos a trabajar con la estructura modelo, vista controlador

# Nos vamos a apoyar de la clase Blueprint
# Esta clase nos permite trabajar con aplicaciones modulables
from flask import Blueprint
from flask import render_template, request, flash, redirect, url_for

from flask_login import login_user, logout_user, login_required, current_user
from . import login_manager
from .models import User
# Importo el formulario de LogIn
from .forms import LoginForm, RegisterForm
# Realizamos una instancia
# El primer argumento es el nombre de nuestro contexto
# El segundo argumento es el contexto del cual se está creando la instancia
page = Blueprint('page', __name__)

@login_manager.user_loader
def load_user(id):
	return User.get_by_id(id)

# Declaramos una función la cual se va a ejecutar en caso de que no se encuentre la página
# La función recibe un arguento, este es el error
# Por buenas prácticas regresamos dos valores
# El primer valor a regresar es lo que queremos retornar
# El segundo valor es un número o código que indique el tipo de error que se generó
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


# Declaramos la función de Login
# Por defecto flask permite que las peticiones sólo sean con el método get
# Mediante una lista indicamos los métodos que queremos utilizar
# El método GET me permitirá mostrar en pantalla el formulario
# El método POST nos permite crear una nueva sesión
@page.route('/login', methods=['GET', 'POST'])
def login():

	# Si el usuario ya está autenticado no me muestra esta página
	if current_user.is_authenticated: # Usuario actual
		return redirect(url_for('.tasks'))

	# Creo una instancia del formulario de LoginForm
	# El formulario se crear con atributos vacíos por defecto
	# request.form nos permite saber si el usuario envió información
	# De esta manera creo la instancia con dicha infomración
	form = LoginForm(request.form)

	# Verificamos si la petición fue realizada con el método post
	# form.validate nos regresa un booleano, regresa True si todas las validaciones fueron hechas correctamente
	if request.method == 'POST' and form.validate():
		user = User.get_by_username(form.username.data)
		if user and user.verify_password(form.password.data):
			login_user(user)
			flash('Usuario autenticado exitosamente')
		else:
			flash('Usuario o contraseña incorrecta', 'error')
			
	# Le paso como argumento al parámetro form la instancia form
	return render_template('auth/login.html', title='Login', form=form)

@page.route('/register', methods=['GET', 'POST'])
def register():

	# Si el usuario ya está autenticado no me muestra esta página
	if current_user.is_authenticated: # Usuario actual
		return redirect(url_for('.tasks'))

	form = RegisterForm(request.form)

	# Verifico si el usuario envió información
	if request.method == 'POST':
		# Si el usuario mandó información compruebo que sea válida
		if form.validate():
			# Creo un usuario
			user = User.create_element(form.username.data, form.password.data, form.email.data)
			flash('Usuario creado de forma exitosa')
			# print(user.id)
			login_user(user)
			return redirect(url_for('.tasks'))
			
	return render_template('auth/register.html', title='Registro', form=form)

@page.route('/logout')
def logout():
	logout_user()
	flash('Cerraste sesión exitosamente')
	return redirect(url_for('.login'))

# Esta URL nos permite listar las tareas de un usuario
# Para hacer uso de esta URL es necesario estar autenticado
@page.route('/tasks')
@login_required
def tasks():
	return render_template('task/list.html', title='Tareas')