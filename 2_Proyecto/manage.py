# Importamos el módulo previamente creado
from app import create_app
from flask_script import Manager


# Importamos el archivo de configuración
from config import config

config_class = config['development']

# Creamos la instancia
app = create_app(config_class)

# Para levantar el servidor usamos flask script
# pip install Flask-Script
# Esto nos ayudará a tener un proyecto generalizado
# Los formularios, modelos, vistas, etc. Se encontrarán en carpetas diferentes
# Esto nos ayuda a que si en un futuro queremos modificar componentes podemos hacerlo de una forma más sencilla
# Quizá el primer paso, el de crear la estructura sea el más pesado
# Ejecutamos el servidor de la siguiente manera

# python manage.py runserver




if __name__ == '__main__':
	manager = Manager(app)
	manager.run()

