import sys

sys.path.insert(0, '/var/www/app') # Agrego la ruta donde python busca los modulos, que es donde se encuentra mi aplicacion. Necesario para que apache pueda acceder a la app.

from app import app as application #Esta línea importa el objeto app desde el módulo app.py, que debe estar ubicado en el directorio /var/www/html/app. 
                                   #Este objeto app es la instancia de la aplicación Flask.
                                   # Se renombra a application porque es el nombre que Apache espera para ejecutar la aplicación usando WSGI.
#Este archivo actua como puente entre apache y mi aplicacion flask.
