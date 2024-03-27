"""
Django settings for NewsPortal project.

Generated by 'django-admin startproject' using Django 5.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
<<<<<<<< HEAD:Django/project/project/settings.py
SECRET_KEY = 'django-insecure-b9%&q)vd6&s78*&9gz7=un)_y(l8yj35bw(-cq-08qk5jx48jx'
========
SECRET_KEY = 'django-insecure-9fi^8zt$a3y=wq+xzv)x$1z1n(3@j+ts6%5=&e4acw_9tvr)k!'
>>>>>>>> 0d784d71d88347ac506b58de87d1bfce38be5f4f:Django/project_1/NewsPortal/NewsPortal/settings.py

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
<<<<<<<< HEAD:Django/project/project/settings.py
    'django.contrib.sites',
    'django.contrib.flatpages',
    'simpleapp',
]

SITE_ID = 1

========
    'news',
]

>>>>>>>> 0d784d71d88347ac506b58de87d1bfce38be5f4f:Django/project_1/NewsPortal/NewsPortal/settings.py
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
<<<<<<<< HEAD:Django/project/project/settings.py
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware'
]

ROOT_URLCONF = 'project.urls'
========
]

ROOT_URLCONF = 'NewsPortal.urls'
>>>>>>>> 0d784d71d88347ac506b58de87d1bfce38be5f4f:Django/project_1/NewsPortal/NewsPortal/settings.py

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

WSGI_APPLICATION = 'NewsPortal.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
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
<<<<<<<< HEAD:Django/project/project/settings.py

STATICFILES_DIRS = [
    BASE_DIR / "static"
]
========
>>>>>>>> 0d784d71d88347ac506b58de87d1bfce38be5f4f:Django/project_1/NewsPortal/NewsPortal/settings.py
