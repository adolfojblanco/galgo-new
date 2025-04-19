from .base import *

SECRET_KEY = "django-insecure-vu0872#b-96k3zu+97r%p4&y8r#v2xomn@b4a5nn(^-=n4!!es"

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=1),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
}

DEBUG = True

ALLOWED_HOSTS = ['*']

CSRF_TRUSTED_ORIGINS = ["http://localhost:4200"]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:4200",
]


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}