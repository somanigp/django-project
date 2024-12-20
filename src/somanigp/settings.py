"""
Django settings for somanigp project.

Generated by 'django-admin startproject' using Django 5.0.9.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
# import os # * Use Operating System that Python has access to.
from pathlib import Path
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# print("BASE_DIR", BASE_DIR)  # D:\Govind's Library\projects\django-project\src

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# * If DJANGO_SECRET_KEY not provided then decouple breaks the application.
# ! python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
SECRET_KEY = config("DJANGO_SECRET_KEY")
# print(SECRET_KEY)
# SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-)&j2t@j)4dgbh)zqq2(pm$0p2ys7m@ko8l$60wp@0ddai3$ou!')

# SECURITY WARNING: don't run with debug turned on in production!
# * cmd to include environment variable : DJANGO_DEBUG=True python manage.py runserver
# * echo $DJANGO_DEBUG  # To see value in terminal
# ! Environment variables are read as or exported as strings.
# DEBUG = os.environ.get("DJANGO_DEBUG").lower() == "true"

# *use with python-decouple. It gives first priority to os env variables and then dotenv file. But can access both thus code remains same
# * unset DJANGO_DEBUG # Helps remove environment variable
DEBUG = config("DJANGO_DEBUG", cast=bool, default=False)  # DJANGO_DEBUG=True or 1 // False or 0. Both works.

# print("DEBUG", DEBUG)

# On which servers this application can be run
ALLOWED_HOSTS = [
    # * initial . means sub-domains are allowed
    ".railway.app", # https://xy.prod.railway.app is allowed.
]

# DEBUG is True for local only and thus adding localhost to ALLOWED_HOSTS list when running in local.
if DEBUG:
    ALLOWED_HOSTS += [
        "127.0.0.1",
        "localhost"
    ]

# Application definition : !* Smaller components that make the project 

INSTALLED_APPS = [
    # django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # my-apps
    'visits',  # Adding a model
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'somanigp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        #** Add paths for it to check if templates are stored there.
        'DIRS': [BASE_DIR / "templates", BASE_DIR / "other_paths"],
        'APP_DIRS': True,
        # * When templates are rendered below variables it can directly use.
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

WSGI_APPLICATION = 'somanigp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
# python manage.py migrate
# Operations to perform:
#   Apply all migrations: admin, auth, contenttypes, sessions, visits
# Running migrations:
#   No migrations to apply. # * When no changes to database mapping needed.

DATABASES = {
    # By default - local database. django will by default create a sqlite3 database if one doesn't exist. Migrate command applies changes to database and creates it in local if it doesn't exist.
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
