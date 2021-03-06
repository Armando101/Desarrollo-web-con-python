# Este archivo almacenará los diferentes modelos que vamos a utilizar en el proyecto
import datetime
# Esta función nos genera un hash para la contraseña
# pip install wekzeug
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

from flask_login import UserMixin

# El punto hace referencia a este módulo
from . import db

# Esta clase será la representación de la tabla users
# Para trabajar la clase como un modelo, tendrá que heredar de models
class User(db.Model, UserMixin):
	# Los atributos son las columnas de la tabla
	# Definimos el tipo de dato con la función Column
	# También podemos definir los constraints

	# Colocamos el nombre de la tabla que queremos que se cree
	__tablename__ = 'users'

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(50), unique=True, nullable=False)
	encypted_password = db.Column(db.String(100), nullable=False)
	email = db.Column(db.String(100), unique=True, nullable=False)

	# Este atributo nos permite saber cuando un registro fue creado
	# Cada que se cree un nuevo registro se guardará la fecha exacta en la que fue creado.
	create_at = db.Column(db.DateTime, default=datetime.datetime.now())

	# Esta función recibe dos passwords
	# Uno encriptado y el otro en texto plano
	def verify_password(self, password):
		return check_password_hash(self.encypted_password, password)

	@property
	def password(self):
		pass

	# Usamos la propiedad setter para colocar el valor
	@password.setter
	def password(self, value):
		# Pasamos la contraseña en texto plano a la función generate_password_hash
		self.encypted_password = generate_password_hash(value)


	def __str__(self):
		"""
			Cada que se haga una impresion de un User
			Se visualizará su username
		"""
		return self.username

	@classmethod
	# No coloco id ni create_at porque se crean automáticamente
	def create_element(cls, username, password, email):
		user = User(username=username, password=password, email=email)

		# Agregamos el usuario a la base de datos
		db.session.add(user)
		# Confirmamos los cambios a la base de datos
		db.session.commit()

		return user

	# Método que nos permite no crear varios usuarios con el mismo username
	# Si el usuario existe obtenemos una instancia de la clase User
	# Si el usuario no existe tenemos un none
	@classmethod
	def get_by_username(cls, username):
		return User.query.filter_by(username=username).first()


	# Validación de email
	@classmethod
	def get_by_email(cls, email):
		return User.query.filter_by(email=email).first()
	
	@classmethod
	def get_by_id(cls, id):
		return User.query.filter_by(id=id).first()


