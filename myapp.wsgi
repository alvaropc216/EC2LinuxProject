import sys
sys.path.insert(0, '/var/www/Video-Game-Catalog')
from videogames import app as application
application.secret_key='super-secret_key'
