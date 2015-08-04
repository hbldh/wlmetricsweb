import os
from os import environ

try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse

CSRF_ENABLED = True

if os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'local_config.py')):
    from wlmetricsweb.local_config import *
else:
    SECRET_KEY = environ.get('SECRET_KEY')

    # Mongolab
    mongolab_uri = environ.get('MONGOLAB_URI')
    if mongolab_uri:
        url = urlparse(mongolab_uri)
        MONGO_URI = mongolab_uri
        MONGODB_USER = url.username
        MONGODB_PASSWORD = url.password
        MONGODB_HOST = url.hostname
        MONGODB_PORT = url.port
        MONGODB_DB = url.path[1:]

    STORMPATH_API_KEY_ID = environ.get('STORMPATH_API_KEY_ID')
    STORMPATH_API_KEY_SECRET = environ.get('STORMPATH_API_KEY_SECRET')
    STORMPATH_APPLICATION = os.path.basename(environ.get('STORMPATH_URL'))
