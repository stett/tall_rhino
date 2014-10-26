from .dev import *

BASE_DOMAIN = 'http://localhost:8000'
SITE_ID = 1

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'tall_rhino_dev_stett.db',
        'USER': 'stett',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}
