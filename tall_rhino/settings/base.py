import os
from unipath import Path
from django.core.exceptions import ImproperlyConfigured


# Base project directory
PROJECT_ROOT = Path(__file__).ancestor(3)
REPOSITORY_ROOT = Path(__file__).ancestor(3)

# Secret settings
from .secret import *

# Set the user model
#AUTH_USER_MODEL = 'users.User'


# Allowed host names... if blank, all are allowed. This should be
# specified at least in prod.py if not in dev.py as well.
ALLOWED_HOSTS = []


# Application definition
INSTALLED_APPS = (

    # Django Core
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # Tall Rhino Core
    'blog',

    # Third Party
    'south',
    #'braces',
    'rest_framework',
    'compressor',
    'sorl.thumbnail',
    'disqus',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_DIRS = (
    'tall_rhino/templates/',
)
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)


# Context processors
TEMPLATE_CONTEXT_PROCESSORS = (

    # Default context processors
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",

    # Custom context processors
)


# Static files finders/compilers
STATICFILES_FINDERS = (

    # Core Django
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',

    # Other
    'compressor.finders.CompressorFinder',
)

STATICFILES_DIRS = (

    'tall_rhino/static/',
)


# REST framework settings
REST_FRAMEWORK = {

    'DEFAULT_PERMISSION_CLASSES': [
        #'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
        'rest_framework.permissions.IsAuthenticated',
    ],

    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    )
}


# Set the named views for loggin in and out
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'


#
ROOT_URLCONF = 'tall_rhino.urls'
WSGI_APPLICATION = 'tall_rhino.wsgi.application'


# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
STATIC_URL = '/static/'


# Media files (user uploaded content)
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')
MEDIA_URL = '/media/'


# Log files
LOG_ROOT = os.path.join(REPOSITORY_ROOT, 'log')
LOGGING = {
    'version': 1,
    'handlers': {
        'debug-file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOG_ROOT, 'django-debug.log')
        },
    },
    'loggers': {
        'log': {
            'handlers': [ 'debug-file', ],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}


# Compressor settings
COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True
COMPRESS_PRECOMPILERS = (
    ('text/less', 'lessc {infile} {outfile}'),
)

# Disqus settings
DISQUS_API_KEY = 'HV7aw0Ex8nbmn7Fmfm2lLsWBHGCiVZKouMNaOvjfXbXzaZKnQqVeFf9ErPIwcWRq'
DISQUS_WEBSITE_SHORTNAME = 'tallrhinoceros'
