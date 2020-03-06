from flask import Flask

# Importamos Bootstrap
from flask_bootstrap import Bootstrap

# Hcemos una instancia
app = Flask(__name__)

# Creamos una instancia de Bootstrap
bootstrap = Bootstrap()

# El punto indica que vamos a importar de un archivo
from .views import page

# Generamos una función la cual retorna nuestra instancia
# Esto para que cada vez que se importe el módulo trabajemos con la misma instancia
def create_app(config):

	app.config.from_object(config)

	# Indicamos que el servidor puede utilizar bootstrap
	bootstrap.init_app(app)

	# Indicamos al servidor las rutas que utilizará
	app.register_blueprint(page)
	return app














