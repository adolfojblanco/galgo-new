from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-p#%z@(395i-^0d)#7rbel47t96)oj*@yhgu$97zi@gtsfreo5_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'galgo-test',
        'USER': 'adolfob',
        'PASSWORD': 'Emma2023*',
        'HOST': 'server.adbwebdesign.com',
        'PORT': '5432',
    }
}