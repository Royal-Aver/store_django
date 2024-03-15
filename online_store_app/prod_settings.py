from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-wxzu67.rh-e^mh*=$#)-u657hhg+17$a*t(x^%8aaqffhfhgfbbwae%"

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']



STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
