from .common import *
import os

SECRET_KEY = os.environ['SECRET_KEY']
DEBUG =False

ALLOWED_HOSTS = ['urmi-prod.herokuapp.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR  / 'db.sqlite3',
    }
}