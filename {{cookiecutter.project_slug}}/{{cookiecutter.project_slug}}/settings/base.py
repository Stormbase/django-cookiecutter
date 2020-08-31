"""
Base settings for the application.

"""

import os

import environ
from django.utils.translation import gettext_lazy as _

from .logging import *  # noqa

env = environ.Env()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


DEBUG = env.bool("DEBUG", default=False)

# Read the .env file if it exists and we are in debug mode
if os.path.exists(os.path.abspath(os.path.join(BASE_DIR, "..", ".env"))):
    environ.Env.read_env(os.path.abspath(os.path.join(BASE_DIR, "..", ".env")))

# Change this secret in production!
SECRET_KEY = env.str("SECRET_KEY", default="")

# Setting this environment variable in production is highly recommended
# See: https://docs.djangoproject.com/en/3.0/ref/settings/#allowed-hosts
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["*"])

# Application definition

INSTALLED_APPS = [
    "whitenoise.runserver_nostatic",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # {{cookiecutter.project_slug}}
    "{{cookiecutter.project_slug}}",
    "{{cookiecutter.project_slug}}.hello",
    "{{cookiecutter.project_slug}}.user",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "{{cookiecutter.project_slug}}.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {"default": env.db_url(default="postgres://localhost/{{cookiecutter.project_slug}}")}


# Cache
# https://docs.djangoproject.com/en/3.0/ref/settings/#std:setting-CACHES

CACHES = {"default": env.cache(default="dummycache://")}


# Email
# https://docs.djangoproject.com/en/3.0/ref/settings/#std:setting-EMAIL_HOST

DEFAULT_FROM_EMAIL = env.str(
    "DEFAULT_FROM_EMAIL", default="Example <hello@example.org>"
)
EMAIL_HOST = env.str("EMAIL_HOST", default="localhost")
EMAIL_HOST_USER = env.str("EMAIL_HOST_USER", default="")
EMAIL_HOST_PASSWORD = env.str("EMAIL_HOST_PASSWORD", default="")
EMAIL_PORT = env.int("EMAIL_PORT", default=1025)

EMAIL_SUBJECT_PREFIX = env.str("EMAIL_SUBJECT_PREFIX", default="[Django]")


# Authentication
# https://docs.djangoproject.com/en/3.0/topics/auth/customizing/

# Use our own User model
# This setting cannot be changed without causing chaos!
AUTH_USER_MODEL = "user.User"


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = "en-us"

LANGUAGES = [("en", _("English"))]

TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
# https://whitenoise.readthedocs.io/en/stable/django.html

STATIC_URL = env.str("STATIC_URL", default="/static/")
STATIC_ROOT = os.path.join(BASE_DIR, "public/static")
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# File storage for user-uploaded files
# https://docs.djangoproject.com/en/3.0/ref/settings/#std:setting-MEDIA_URL
# https://docs.djangoproject.com/en/3.0/ref/settings/#std:setting-MEDIA_ROOT
MEDIA_URL = env.str("MEDIA_URL", default="/media/")
MEDIA_ROOT = os.path.join(BASE_DIR, "public/media")

# Web Server Gateway Interface (WSGI). Used for deployment
# https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
WSGI_APPLICATION = "{{cookiecutter.project_slug}}.wsgi.application"
