# Este archivo almacenará los diferentes modelos que vamos a utilizar en el proyecto
import datetime

# El punto hace referencia a este módulo
from . import db

# Esta clase será la representación de la tabla users
# Para trabajar la clase como un modelo, tendrá que heredar de models
class User(db.Model):
	# Los atributos son las columnas de la tabla
	# Definimos el tipo de dato con la función Column
	# También podemos definir los constraints

	# Colocamos el nombre de la tabla que queremos que se cree
	__tablename__ = 'users'

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(50), unique=True, nullable=False)
	password = db.Column(db.String(93), nullable=False)
	email = db.Column(db.String(100), unique=True, nullable=False)

	# Este atributo nos permite saber cuando un registro fue creado
	# Cada que se cree un nuevo registro se guardará la fecha exacta en la que fue creado.
	create_at = db.Column(db.DateTime, default=datetime.datetime.now())

	def __str__(self):
		"""
			Cada que se haga una impresion de un User
			Se visualizará su username
		"""
		return self.username