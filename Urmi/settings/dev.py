from .common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-oj23yf7ybs6fcu82(b_zt&t0!@4nf0m9fngdc925jr=&orgf*v'

DEBUG =True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR  / 'db.sqlite3',
    }
}