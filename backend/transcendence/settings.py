"""
Django settings for transcendence project.

Generated by 'django-admin startproject' using Django 5.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-_0@qbs8*u@@s(#=4@e8yol-y4spd)%ymko!-ja^#fs=jofyf!)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

INTERNAL_IPS = [
	'127.0.0.1',
]

from corsheaders.defaults import default_headers

CORS_ALLOW_ORIGINS = [
	'http://localhost',
	'https://localhost',
	'http://localhost:8000',
	'https://localhost:8000',
	'http://127.0.0.1',
	'https://127.0.0.1',
	'http://127.0.0.1:8000',
	'https://127.0.0.1:8000',
]

CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_HEADERS = list(default_headers) + [
	'X-42-Token',
]


# Application definition

INSTALLED_APPS = [
	'corsheaders',
	'quiz.apps.QuizConfig',
	'pong.apps.PongConfig',
	'chat.apps.ChatConfig',
	'dashboard.apps.DashboardConfig',
	'channels',
	'daphne',
	'user_management.apps.UserManagementConfig',
	'rest_framework',
	'crispy_forms',
	'crispy_bootstrap4',
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
]

MIDDLEWARE = [
	'corsheaders.middleware.CorsMiddleware',
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.locale.LocaleMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

import os
import secrets
import sys

TESTING = 'test' in sys.argv
if not TESTING:
	INSTALLED_APPS = [
		*INSTALLED_APPS,
		'debug_toolbar',
	]
	MIDDLEWARE = [
		'debug_toolbar.middleware.DebugToolbarMiddleware',  # early, but after encoding response content
		*MIDDLEWARE,
	]

ROOT_URLCONF = 'transcendence.urls'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [BASE_DIR / 'templates'],  # This line should point to the 'templates' directory
		# 'DIRS': [],
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

WSGI_APPLICATION = 'transcendence.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
	# for production
	# 'default': {
	#     "ENGINE": "django.db.backends.postgresql",
	#     "NAME": "postgres",
	#     "USER": "postgres",
	#     "PASSWORD": Path("/var/run/secrets/postgres_password").read_text(),
	#     "HOST": "postgres",
	#     "PORT": "5432",
	# }
	# for development
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': BASE_DIR / 'db.sqlite3',
	}
}

# for 42 api - enables requesting bearer token: requires running Makefile to export the variable(s)
import platform

if platform.system() == 'Darwin':  # macOS
	SECRETS_PATH = Path('../secrets/')
	REMOTE_OAUTH_SECRET = Path(SECRETS_PATH / 'oauth_api_secret').read_text().strip()

	def get_env_variable(env, key):  # dotenv would not install for some reason
		return next(
			(
				line.split('=', 1)[1].strip()
				for line in env.splitlines()
				if line.startswith(key + '=')
			),
			None,
		)

	CLIENT_ID = get_env_variable(
		env=Path(SECRETS_PATH / '.env').read_text(), key='REMOTE_OAUTH_UID'
	)
else:  # Assume Linux (Docker)
	REMOTE_OAUTH_SECRET = Path('/var/run/secrets/oauth_api_secret').read_text().strip()
	CLIENT_ID = os.getenv('REMOTE_OAUTH_UID')
if REMOTE_OAUTH_SECRET is None:
	raise ValueError('Environment variable REMOTE_OAUTH_UID is not set')
if CLIENT_ID is None:
	raise ValueError('Secret oauth_api_secret is not set')
SECRET_STATE = secrets.token_urlsafe(32)

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

TIME_ZONE = 'CET'

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [
	BASE_DIR / 'static',
	BASE_DIR / 'quiz/static',
	BASE_DIR / 'dashboard/static',
	BASE_DIR / 'pong/static',
]

STATIC_ROOT = BASE_DIR / 'staticfiles'

import os

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGIN_REDIRECT_URL = '/dashboard/'

LOGIN_URL = '/login/'

AUTH_USER_MODEL = 'user_management.CustomUser'

ASGI_APPLICATION = 'transcendence.asgi.application'

CHANNEL_LAYERS = {'default': {'BACKEND': 'channels.layers.InMemoryChannelLayer'}}

from django.utils.translation import gettext_lazy as _

LANGUAGES = [
	('en', _('English')),
	('sv', _('Swedish')),
	('de', _('German')),
]

LOCALE_PATHS = [
	BASE_DIR / 'locale',
]

USE_I18N = True
USE_L10N = True
