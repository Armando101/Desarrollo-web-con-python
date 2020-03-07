class Config:
	# Llave secrete para generar tokens y autenticar los formularios
	SECRET_KEY = 'Armando'

# Colocamos las configuraciones necesarias para el servidor
class DevelopmentConfig(Config):
	DEBUG = True


# Generamos un diccionario
# Declaramos los entornos a utilizar
# development y por default
# Hasta este punto este archivo es básico y sencillo
# Cuando utilicemos bases de datos, migraciones, etc este archivo será de mayor utilidad
config = {
	'development': DevelopmentConfig,
	'default': DevelopmentConfig
}