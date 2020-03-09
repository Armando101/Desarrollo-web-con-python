# Para crear formularios nos apoyamos de la librería WTForms
# pip install WTForms

# Importamos la clase forms
from wtforms import Form
# El siguiente módulo nos permite hacer validaciones a formularios
from wtforms import validators
from wtforms import StringField, PasswordField, BooleanField
from wtforms.fields.html5 import EmailField

# Esta clase nos permitirá crear un formulario de LogIn
class LoginForm(Form):
	# Declaramos los atributos
	# Estos atributos son objetos de tipo:
	# StringField: permite mostrar el texto
	# PasswordField: oculta el texto
	# El segundo parámetro es una lista, esta lista contiene las funciones que queremos validar
	username = StringField('Username', [
			# Indicamos que la longitud debe ser mínimo 4 y máximo 50
			# También podemos incluir un mensaje personalizado en caso de que la validación no se cumpla
			validators.length(min=4, max=50, message='El username se encuentra fuera de rango'),
			validators.Required(message="Ingrese un username")
		])
	password = PasswordField('Password', [
			# Indicamos que tiene que no se puede dejar vacío este espacio
			validators.Required(message="El password es requerido")
		])


class RegisterForm(Form):
	username = StringField('Username', [
			validators.length(min=4, max=50),
			validators.Required(message="Ingrese un username")
		])
	email = EmailField('Email', [
			validators.length(min=6, max=100),
			validators.Required(message='El email es requerido'),

			# Verificamos que el email sea válido
			# La función Email usa su propia expresión regular para verificar esto
			validators.Email(message='Ingrese un email válido')
		])

	password = PasswordField('Password', [
			validators.Required(message='El password es requerido'),
			validators.EqualTo('confirm_password', message='La contraseña no coincide')
		])

	# Confiramamos la contraseña
	confirm_password = PasswordField('Confirm password')

	accept = BooleanField('Acepto términos y condiciones', [
			validators.DataRequired()
		])
