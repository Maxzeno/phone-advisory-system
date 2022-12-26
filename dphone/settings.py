"""
Django settings for dphone project.

Generated by 'django-admin startproject' using Django 3.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""
from decouple import config
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(int(config('DEBUG', 0)))

# _DEPLOY = False

# use local db, storage, email config create be me
_TRY_LOCAL_DB = bool(int(config('_TRY_LOCAL_DB', 0)))
_TRY_LOCAL_STORAGE = bool(int(config('_TRY_LOCAL_STORAGE', 0)))
_TRY_LOCAL_EMAIL = bool(int(config('_TRY_LOCAL_EMAIL', 0)))

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

_ALLOWED_HOST = config('ALLOWED_HOST')
if _ALLOWED_HOST:
    ALLOWED_HOSTS.append(_ALLOWED_HOST)

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'main',
    'user',
    'registration',
    'manage',
]

if not _TRY_LOCAL_STORAGE:
    INSTALLED_APPS.append('cloudinary')
    INSTALLED_APPS.append('cloudinary_storage')


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',

]

ROOT_URLCONF = 'dphone.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'registration/templates'),
            os.path.join(BASE_DIR, 'user/templates'),
            os.path.join(BASE_DIR, 'main/templates'),
            ],
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

WSGI_APPLICATION = 'dphone.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

if _TRY_LOCAL_DB:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }


else:
    DATABASES = {
        'default': {
            'ENGINE': config('DATABASES_DEFAULT_ENGINE'),
            'NAME': config('DATABASES_DEFAULT_NAME'),
            'HOST': config('DATABASES_DEFAULT_HOST'),
            'PORT': int(config('DATABASES_DEFAULT_PORT')),
            'USER': config('DATABASES_DEFAULT_USER'),
            'PASSWORD': config('DATABASES_DEFAULT_PASSWORD'),
        }
    }


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'    

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/dphone')


if not _TRY_LOCAL_STORAGE:

    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

    CLOUDINARY_STORAGE = {
        'CLOUD_NAME': config('CLOUDINARY_STORAGE_CLOUD_NAME'),
        'API_KEY': config('CLOUDINARY_STORAGE_API_KEY'),
        'API_SECRET': config('CLOUDINARY_STORAGE_API_SECRET')
    }




CRISPY_TEMPLATE_PACK = 'bootstrap4'


###DEVELOPMENT
if _TRY_LOCAL_EMAIL:
    EMAIL_HOST = 'localhost'
    EMAIL_PORT = '1025'

###PRODUCTION
else:
    EMAIL_HOST = config('EMAIL_HOST', 'smtp.gmail.com')
    EMAIL_HOST_USER = config('EMAIL_HOST_USER', 'nwaegunwaemmauel@gmail.com')
    EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
    EMAIL_PORT = config('EMAIL_PORT', '587')
    EMAIL_USE_TLS = bool(config('EMAIL_USE_TLS', True))


LOGIN_URL = '/signin/'
