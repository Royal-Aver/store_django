from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-wxzu6@yrh-e^mh*=$#)-uwz0zm+17$a*t(x^%8aaqf6jt4wge%"

DEBUG = True

ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]