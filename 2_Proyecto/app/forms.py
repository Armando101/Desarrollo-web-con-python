# Para crear formularios nos apoyamos de la librería WTForms
# pip install WTForms

# Importamos la clase forms
# La clase HiddenField nos permite ocultar campos al usuario
from wtforms import Form, HiddenField
# El siguiente módulo nos permite hacer validaciones a formularios
from wtforms import validators
from wtforms import StringField, PasswordField, BooleanField
from wtforms.fields.html5 import EmailField

from .models import User

# Función de validación
def nombre_validator(form, field):
	if field.data == 'nombre':
		raise validators.ValidationError('EL username nombre no es permitido')

# Esta función nos permite prevenir ataques creando cuentas innecesarias
# Si algún tipo de bot quiere generar usuarios inválidos hará la petición enviando valores para todos los campos (No sabrá diferenciar entre un campo oculto y uno visible). Al recibir un valor en el campo honeypot, un valor que no se espera por parte de un usuario normal, la validación será inválida.
def length_honeypot(form, field):
	if len(field.data) > 0:
		raise validators.ValidationError('Sólo los humanos pueden completar el registro')

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
			validators.Required(message="Ingrese un username"),
			nombre_validator
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

	honeypot = HiddenField("", [length_honeypot])

	# Este método me permite verificar que los usernames no se repitan
	def validate_username(self, username):
		if User.get_by_username(username.data):
			raise validators.ValidationError('El username ya se encuentra en uso.')

	def validate_email(self, email):
		if User.get_by_email(email.data):
			raise validators.ValidationError('El email ya se encuentra en uso.')

	# Sobreescribimos la función validate que se encuentra en views.py
	# Esto para personalizar las validaciones
	def validate(self):
		# Si un campo no cumple con por lo menos una validación regresamos false
		if not Form.validate(self):
			return False

		if len(self.password.data) < 8:
			self.password.errors.append('El password es demasiado corto')
			return False

		return True