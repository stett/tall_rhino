from .base import *

DEBUG = True
TEMPLATE_DEBUG = False
THUMBNAIL_DEBUG = False

COMPRESS_OFFLINE = True
COMPRESS_CSS_FILTERS = []
COMPRESS_JS_FILTERS = []

ALLOWED_HOSTS = ['tallrhinoceros.com', 'dev.tallrhinoceros.com', 'prod.tallrhinoceros.com', 'localhost', '127.0.0.1']

BASE_DOMAIN = 'http://tallrhinoceros.com'
SITE_ID = 2

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'tall_rhino',
        'USER': 'tall_rhino',
        'PASSWORD': 'KR7Ey+"AqY"9g-vBQ&UaYj?3ShxY@4',
        'HOST': 'localhost',
        'PORT': '',
    }
}
