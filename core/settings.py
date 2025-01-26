"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 5.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# pip install python-decouple
from decouple import config

from datetime import timedelta

# pip install dj-database-url
import dj_database_url


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-(x5_^%xb^0f^3f0e_2$i!!8gup^+sruewtd_y)zg$em$*(mfgt'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    # For Custom Admin Interface
    'admin_interface',
    'colorfield',
    #----------------#
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party apps
    'taggit',
    'phonenumber_field',
    'django_countries',
    
    "authentication",
    "location",
    "messaging",
    "favorites",
    "listing",
    "search",
    "theme",
    'pages',

    "users",
   
    # Django Allauth
    'django.contrib.sites',  # Obligatoire pour django-allauth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.linkedin_oauth2',
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # for production static files 
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',  # middleware
   
]

ROOT_URLCONF = 'core.urls'

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
                
                # Custom context processors for listing app / categories & subcategories
                'listing.context_processors.categories_processor',

            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# Configuration de la base de données
# if DEBUG:
#     # Base de données de développement
#     DATABASE_URL = config(
#         'DEV_DATABASE_URL',
#         default= 'sqlite:///' + str(BASE_DIR / 'db.sqlite3')
#     )
# else:
#     # Base de données de production
#     DATABASE_URL = config(
#         'PROD_DATABASE_URL',
#         default= ''
#     )

DATABASE_URL='sqlite:///db.sqlite3'
DATABASES = {
    'default': dj_database_url.parse(
        DATABASE_URL,
        conn_max_age=600,
        conn_health_checks=True
    )
}

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
#STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static'
]
#STATIC_ROOT = BASE_DIR / 'staticfiles'
STATIC_ROOT = BASE_DIR / "assets"

# for production static files
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'



# Media files (Images, Videos, etc)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')
# MEDIA_URL = '/uploads/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Custom User Model
AUTH_USER_MODEL = 'authentication.User'


# Make tags case insensitive
TAGGIT_CASE_INSENSITIVE = True

# # Configure tag string parsing
# TAGGIT_TAGS_FROM_STRING = 'custom_tags.tag_splitter'  # Your custom parsing function

# # Configure tag string representation
# TAGGIT_STRING_FROM_TAGS = 'custom_tags.tag_joiner'    # Your custom joining function

# Configuration pour phonenumber_field
PHONENUMBER_DB_FORMAT = "E164"     # Format de stockage en base

# Configuration Django Allauth
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

SITE_ID = 1

# Paramètres de configuration Allauth
ACCOUNT_AUTHENTICATION_METHOD = 'email'  # Utiliser l'email pour l'authentification
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'  # ou 'optional' ou 'none'
ACCOUNT_USERNAME_REQUIRED = False
LOGIN_REDIRECT_URL = '/'  # Redirection après connexion
LOGOUT_REDIRECT_URL = '/'  # Redirection après déconnexion

# Configuration email (à adapter selon votre configuration)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # Pour le développement

# Configuration des providers sociaux
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': config('GOOGLE_CLIENT_ID'),
            'secret': config('GOOGLE_SECRET'),
            'key': ''
        },
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    },
    'facebook': {
        'APP': {
            'client_id': config('FACEBOOK_CLIENT_ID'),
            'secret': config('FACEBOOK_SECRET'),
            'key': ''
        },
        'METHOD': 'oauth2',
        'SCOPE': ['email', 'public_profile'],
        'VERSION': 'v15.0'
    },
    'github': {
        'APP': {
            'client_id': config('GITHUB_CLIENT_ID'),
            'secret': config('GITHUB_SECRET'),
            'key': ''
            
        },
        'SCOPE': [
            'user',
            'repo',
            'read:org',
        ],
    },
    'linkedin_oauth2': {
        'APP': {
            'client_id': config('LINKEDIN_CLIENT_ID'),
            'secret': config('LINKEDIN_SECRET'),
            'key': ''
        },
        'SCOPE': ['r_liteprofile', 'r_emailaddress'],
        'PROFILE_FIELDS': [
            'id',
            'first-name',
            'last-name',
            'email-address',
            'picture-url',
            'public-profile-url',
        ]
    }
}


# j'aimerais afficer les clefs dans la console pour les tester
# print(f"Clef Google : {config('GOOGLE_CLIENT_ID')}")
# print(f"Secret Google : {config('GOOGLE_SECRET')}")

