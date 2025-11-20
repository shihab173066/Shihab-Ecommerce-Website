"""
Django settings for ecommerce project.
"""

from pathlib import Path
import os


BASE_DIR = Path(__file__).resolve().parent.parent

# -------------------------------------------------------------
# SECURITY
# -------------------------------------------------------------
SECRET_KEY = 'django-insecure-g*c52-sw60urfkt#)8szop)2tr!imfxsnh%4#4)+@!^zivcjzb'

DEBUG = False

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'shihab-ecommerce-website.onrender.com',
    'shihab-ecommerce-website-1.onrender.com',
]

CSRF_TRUSTED_ORIGINS = [
    'http://localhost:8000',
    'https://shihab-ecommerce-website.onrender.com',
    'https://shihab-ecommerce-website-1.onrender.com',
]

# -------------------------------------------------------------
# APPS
# -------------------------------------------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'store.apps.StoreConfig',
]

# -------------------------------------------------------------
# MIDDLEWARE
# -------------------------------------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # IMPORTANT
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ecommerce.urls'

# -------------------------------------------------------------
# TEMPLATES
# -------------------------------------------------------------
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

# -------------------------------------------------------------
# DATABASE
# -------------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# -------------------------------------------------------------
# PASSWORD VALIDATION
# -------------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# -------------------------------------------------------------
# INTERNATIONALIZATION
# -------------------------------------------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# -------------------------------------------------------------
# STATIC & MEDIA CONFIG (Option A)
# -------------------------------------------------------------

# Static URL
STATIC_URL = '/static/'

# Where collected static files go (Render serves this folder)
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# Project-level static folder (you chose Option A)
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

# WhiteNoise storage
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media files (uploaded images)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# -------------------------------------------------------------
# DEFAULT PRIMARY KEY
# -------------------------------------------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
