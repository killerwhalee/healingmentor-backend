"""
Django Base Configuration

WARNING: Do not use this setting for deployment!

This is the default setting for django project.
You can run a test server only using this configuration.

If you need some change in configuration,
do not change this file directly.

Rather, create other configuration file and import this file.
Then you can freely override the configuration.

Configured by killerwhalee

Github: https://github.com/killerwhalee/healingmentor

"""

from pathlib import Path
import dotenv, os

# Load Environment Variables

dotenv.load_dotenv()


# Base Directory

BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
from django.core.management.utils import get_random_secret_key

SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", get_random_secret_key())


# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = int(os.environ.get("DJANGO_DEBUG", 0))


# Allowed Hosts

ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS", "localhost").split()


# Application Definition

INSTALLED_APPS = [
    # System Application
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # System vendor applications
    "rest_framework",
    "corsheaders",
    "rest_framework_simplejwt",
    # API Endpoints
    "user.apps.UserConfig",
    "session.apps.SessionConfig",
]


# CORS Whitelist

CORS_ORIGIN_WHITELIST = ["http://localhost:3000"]


# Middleware Setting

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# Django REST Framework Settings

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication"
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
    "DEFAULT_FILTER_BACKENDS": [
        "rest_framework.filters.SearchFilter",
        "rest_framework.filters.OrderingFilter",
    ],
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
    ]
    + (["rest_framework.renderers.BrowsableAPIRenderer"] if DEBUG else []),
    "DEFAULT_PARSER_CLASSES": [
        "rest_framework.parsers.JSONParser",
    ],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}


# Django JWT Settings

from datetime import timedelta

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=10),
    "REFRESH_TOKEN_LIFETIME": timedelta(hours=2),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "AUTH_HEADER_TYPES": ("Bearer", "bearer"),
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
}


# Url Configuration

ROOT_URLCONF = "core.urls"


# Templates Setting

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


# WSGI Setting

WSGI_APPLICATION = "core.wsgi.application"


# Database Setting
# Default is SQLite3. Override the setting for other option.

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Customized User Model

AUTH_USER_MODEL = "user.User"


# Password validation

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        "OPTIONS": {
            "min_length": 4,
        },
    },
]


# Registration

LOGIN_REDIRECT_URL = "/"

LOGOUT_REDIRECT_URL = "/"


# Internationalization

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Seoul"

DATE_FORMAT = "Y.m.d"

DATETIME_FORMAT = "Y.m.d h:i A"

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files

STATIC_URL = "/static/"

STATIC_ROOT = BASE_DIR / "_static"


# User Media

MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR / "_media"


# Default primary key field type

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Logging

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse",
        },
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",
        },
    },
    "formatters": {
        "django.server": {
            "()": "django.utils.log.ServerFormatter",
            "format": "[{server_time}] {message}",
            "style": "{",
        },
        "standard": {"format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s"},
    },
    "handlers": {
        "console": {
            "level": "INFO",
            "filters": ["require_debug_true"],
            "class": "logging.StreamHandler",
        },
        "django.server": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "django.server",
        },
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler",
        },
        "file": {
            "level": "INFO",
            "filters": ["require_debug_false"],
            "class": "logging.handlers.RotatingFileHandler",
            "filename": BASE_DIR / "_logs/site.log",
            "maxBytes": 64 * 1024 * 1024,  # 64 MB
            "backupCount": 100,
            "formatter": "standard",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console", "mail_admins", "file"],
            "level": "INFO",
        },
        "django.server": {
            "handlers": ["django.server"],
            "level": "INFO",
            "propagate": False,
        },
    },
}
