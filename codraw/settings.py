import os
import logging
from pathlib import Path
import configparser
from distutils.util import strtobool

config = configparser.ConfigParser()
config.read('/etc/codraw/settings.ini')

PROJECT_APPS = [
    'frontapi',
]

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# BEAUTIFUL HTTPS THINGS, THAT MUST BE USED IN FUTURE
# SECURE_HSTS_SECONDS = ...
# SECURE_SSL_REDIRECT = ...
# SECURE_HSTS_INCLUDE_SUBDOMAINS = ...
# SESSION_COOKIE_SECURE = ...

# Main settings

SECRET_KEY = config['MAIN']['SecretKey']
DEBUG = bool(strtobool(config['MAIN']['Debug']))

ALLOWED_HOSTS = ['*']

# CORS policy

CORS_ORIGIN_ALLOW_ALL = DEBUG
# may I can use only http ?
CORS_ALLOWED_ORIGINS = ['http://127.0.0.1:8080', 'http://localhost:8080']

CORS_EXPOSE_HEADERS = ['Content-Type', 'X-CSRFToken']
CORS_ALLOW_CREDENTIALS = True

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'codraw',
] + list(map(
    lambda proj: f'{proj}.apps.{proj.capitalize()}Config',
    PROJECT_APPS
))

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware', CORS headers is enough?
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'codraw.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'codraw.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'sqlite': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        'OPTIONS': {
            'timeout': 20,
        }
    },
    'postgres': {
        **{option[0].upper(): option[1] for option in config['POSTGRES'].items()},
        'ENGINE': 'django.db.backends.postgresql',
        'default-character-set': 'utf8',
    }
}
DEFAULT_DB = 'sqlite' if DEBUG else 'postgres'
DATABASES['default'] = DATABASES.pop(DEFAULT_DB)

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 8,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'
# STATICFILES_DIRS = [
#     BASE_DIR / "some....",
# ]

# Media filters
MEDIA_ROOT = BASE_DIR
MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# REST Framework

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 12,
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'codraw.utils.filter_backends.BaseOrderingFilterBackend',
    ],
}

# REDIS

REDIS_HOST = config['REDIS']['HOST']
REDIS_PORT = config['REDIS']['PORT']
_REDIS_URL = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0'
BROKER_URL = _REDIS_URL
CELERY_RESULT_BACKEND = _REDIS_URL
BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 3600}

