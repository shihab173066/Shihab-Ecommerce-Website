"""
Django settings for ecommerce project.
... (standard Django header)
"""

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-g*c52-sw60urfkt#)8szop)2tr!imfxsnh%4#4)+@!^zivcjzb'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'shihab-ecommerce-website.onrender.com',
]


CSRF_TRUSTED_ORIGINS = [
    'http://localhost:8000',
    'https://shihab-ecommerce-website.onrender.com',
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'store.apps.StoreConfig', # added app
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # Correctly placed
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ecommerce.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ecommerce.wsgi.application'


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    # ... (omitted for brevity)
]


# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# ----------------------------------------------------------------------
# ✅ FIXED STATIC & MEDIA FILE CONFIGURATION
# ----------------------------------------------------------------------

# 1. Static URL & Root (For WhiteNoise)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# 2. Locations to look for static files (where your 'static' folder is)
# This includes the root static folder used for global assets like CSS/JS.
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

# 3. WhiteNoise Storage (REQUIRED for production styling)
# This handles compression and caching for WhiteNoise.
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# 4. Media URL & Root (For uploaded files like product images)
# The MEDIA_ROOT is where your uploaded files are stored locally (and should be
# committed to Git for this non-S3 setup).
MEDIA_URL = '/media/'
# Based on your previous working directory structure, this is the correct path:
MEDIA_ROOT = os.path.join(BASE_DIR, 'static/images') 
# ----------------------------------------------------------------------


# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'