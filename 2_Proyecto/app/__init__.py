from flask import Flask

# Importamos Bootstrap
from flask_bootstrap import Bootstrap

# Librería para prevenir un ataque de csrf
# pip install Flask-WTF
from flask_wtf.csrf import CSRFProtect
# Hcemos una instancia
app = Flask(__name__)

# Creamos una instancia de Bootstrap
bootstrap = Bootstrap()

# Declaro una instancia
csrf = CSRFProtect()

# El punto indica que vamos a importar de un archivo
from .views import page

# Generamos una función la cual retorna nuestra instancia
# Esto para que cada vez que se importe el módulo trabajemos con la misma instancia
def create_app(config):

	app.config.from_object(config)

	# Asocio la instancia csrf con la aplicación
	csrf.init_app(app)
	# Definimos una llave secreta, esto para generar tokens
	# Los tokens nos servirán para validar la autenticidad de las peticiones, esto lo hacemos en el archivo config.py

	# Indicamos que el servidor puede utilizar bootstrap
	bootstrap.init_app(app)

	# Indicamos al servidor las rutas que utilizará
	app.register_blueprint(page)
	return app














