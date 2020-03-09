class Config:
	# Llave secrete para generar tokens y autenticar los formularios
	SECRET_KEY = 'Armando'

# Colocamos las configuraciones necesarias para el servidor
class DevelopmentConfig(Config):
	DEBUG = True
	# Indico la dirección de la base de datos que voy a utilizar
	# Indico el gestor de base de datos://nombre de usuario con el cuál nos vamos a autenticar:contraseña para autenticarnos @ dirección en la que se encuentra la base de datos / nombre de la base de datos.

	# Si vamos a usar mysql necesitamos instalar:
	# pip install mysqlclient
	# Si surgen problemas con la instalación ejecutar los siguientes comandos:
		# sudo apt-get install python-dev python3-dev 
		# sudo apt-get install libmysqlclient.dev
		# pip install pymysql
		# pip install mysqlclient


	SQLALCHEMY_DATABASE_URI = 'mysql://root:toor@localhost/proyect_web_python'

# Generamos un diccionario
# Declaramos los entornos a utilizar
# development y por default
# Hasta este punto este archivo es básico y sencillo
# Cuando utilicemos bases de datos, migraciones, etc este archivo será de mayor utilidad
config = {
	'development': DevelopmentConfig,
	'default': DevelopmentConfig
}