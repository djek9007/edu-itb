"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 3.2.18.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
from dotenv import load_dotenv
from os import getenv
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(os.path.join(BASE_DIR, '.env'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = getenv('SECRET_KEY')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', 'edu-itb.kz', 'http://edu-itb.kz', 'https://edu-itb.kz', 'www.edu-itb.kz',]


# Application definition

INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',



    'ckeditor',
    'ckeditor_uploader',
    'django_cleanup.apps.CleanupConfig',
    'easy_thumbnails',
    'image_cropping',
    'mptt',
    'menu.apps.MenuConfig',
    'blog.apps.BlogConfig',
]

from easy_thumbnails.conf import Settings as thumbnail_settings

THUMBNAIL_PROCESSORS = (
                           'image_cropping.thumbnail_processors.crop_corners',
                       ) + thumbnail_settings.THUMBNAIL_PROCESSORS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS':[os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': getenv('ENGINE'),
        'NAME': getenv('DBNAME'),
        'USER': getenv('DBUSER'),
        'PASSWORD': getenv('DBPASSWORD'),
        'HOST': getenv('LOCALHOST'),
        'PORT': getenv('DBPORT'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'kk'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
#STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

STATIC_URL = '/static/'
if DEBUG:
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static')
    ]
else:
    STATIC_ROOT = ['/home/c/ci73684/edu-itb.kz/public_html/static/',]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'


STATICFILES_DIRS = [os.path.join(getenv('STATICFILES_DIRS')),]
STATIC_ROOT = getenv('STATIC_ROOT')
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(getenv('MEDIA_ROOT'))

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
CKEDITOR_JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js'
CKEDITOR_UPLOAD_PATH = getenv('CKEDITOR_UPLOAD_PATH')
# CKEDITOR_BASEPATH = getenv('CKEDITOR_BASEPATH')
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'allowedContent': True,
        'extraPlugins': ','.join(
            [
            'youtube',
              'bootstrapTabs',

            ]
        ),
    },
}

EMAIL_HOST = getenv('EMAIL_HOST')
EMAIL_HOST_USER = getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = getenv('EMAIL_HOST_PASSWORD')
EMAIL_PORT = getenv('EMAIL_PORT')
EMAIL_USE_TLS = True