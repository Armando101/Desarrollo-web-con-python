# Para crear formularios nos apoyamos de la librería WTForms
# pip install WTForms

# Importamos la clase forms
from wtforms import Form
# El siguiente módulo nos permite hacer validaciones a formularios
from wtforms import validators
from wtforms import StringField, PasswordField

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
			validators.length(min=4, max=50, message='El username se encuentra fuera de rango')
		])
	password = PasswordField('Password', [
			# Indicamos que tiene que no se puede dejar vacío este espacio
			validators.Required()
		])