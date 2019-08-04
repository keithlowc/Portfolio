"""
Django settings for portfolio project.

Generated by 'django-admin startproject' using Django 2.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import environ

root = environ.Path(__file__) - 2
env = environ.Env(DEBUG=(bool, False), )
env.read_env(env_file=root('.env'))

PRODUCTION_ENV = env.bool('PRODUCTION', default=False)

if PRODUCTION_ENV:
    BASE_DIR = root()
    SECRET_KEY = env('SECRET_KEY')
    DEBUG = env.bool('DEBUG', default=False)
    ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=[])
else:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    SECRET_KEY = '31k61=f^+4^)084x+^vfms(axi%$^3^^lhoy(s)z@mprzwn9@='
    DEBUG = True

ALLOWED_HOSTS = [
    '*',
]

# Application for local development
LOCAL = [
]

# Applications for production deployment
PRODUCTION = [
]

# Applications created by django
COMMON = [
]

# Applications created by you
APPS = [
]

# Default Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
] + COMMON + APPS

if PRODUCTION_ENV:
    INSTALLED_APPS += PRODUCTION
else:
    INSTALLED_APPS += LOCAL

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'portfolio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'portfolio.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

if PRODUCTION_ENV:
    DATABASES = {
        'default': env.db(default='postgres://postgres:postgres@db:5432/postgres',)
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'portfolio',
            'USER': 'web',
            'PASSWORD': 'root',
            'HOST': 'database',
        }
    }

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

# STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'portfolio/static')

# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, "static"),
#     '/var/www/static/',
# ]

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, '../portfolio/static/')

