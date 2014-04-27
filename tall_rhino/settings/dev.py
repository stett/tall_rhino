from .base import *

DEBUG = True
TEMPLATE_DEBUG = True
THUMBNAIL_DEBUG = True

COMPRESS_OFFLINE = False
COMPRESS_CSS_FILTERS = []
COMPRESS_JS_FILTERS = []

BASE_DOMAIN = 'http://dev.tallrhinoceros.com'
SITE_ID = 4

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'tall_rhino_dev',
        'USER': 'stett',
        'PASSWORD': 'O*4[u05y@o2Z1|!',
        'HOST': 'localhost',
        'PORT': '',
    }
}
