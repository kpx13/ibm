# -*- coding: utf-8 -*-
import os
from os.path import abspath, join, dirname

DEBUG = True
TEMPLATE_DEBUG = True

ADMINS = (
)

MANAGERS = ADMINS
PROJECT_ROOT = abspath(join(dirname(__file__), "../"))
LOGIN_URL = '/login'

DATE_FORMAT = '%d.%m.%Y'
DATETIME_FORMAT = '%d.%m.%Y'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'ibm',   # Or path to database file if using sqlite3.
        'USER': 'ibm',                      # Not used with sqlite3.
        'PASSWORD': 'ibm',                  # Not used with sqlite3.
        'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

TIME_ZONE = 'Europe/Moscow'

LANGUAGE_CODE = 'ru-RU'

SITE_ID = 1


USE_I18N = True

USE_L10N = True

MEDIA_ROOT = MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')

MEDIA_URL = '/media/'
ADMIN_TOOLS_THEMING_CSS = 'styles/admin.css'


STATIC_ROOT = STATICFILES_ROOT = os.path.join(PROJECT_ROOT, 'static')


STATIC_URL = STATICFILES_URL = '/static/'
ADMIN_TOOLS_INDEX_DASHBOARD = 'dashboard.CustomIndexDashboard'

STATICFILES_DIRS = (
                    os.path.join(PROJECT_ROOT, 'site_static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = '8bbd(7##fnhjww&_1-m4s_20f@h(av8$ast1c(rtdsp38)2b30'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)
TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.request",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'ibm.urls'

TEMPLATE_DIRS = (
                 os.path.join(PROJECT_ROOT, 'templates'),
)

INSTALLED_APPS = (
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ckeditor',
    'django.contrib.admindocs',
    'sorl.thumbnail',
    'livesettings',

    'pages',
    'gallery',
    'news',
    'partners',
    'links',
)


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

FILE_UPLOAD_MAX_MEMORY_SIZE = 7864320
CKEDITOR_IMAGE_BACKEND = 'Pillow'
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar':
           [
                ['Source',],
                ['Undo', 'Redo', ],
                ['NumberedList','BulletedList','-','Outdent','Indent','Blockquote'],
                ['JustifyLeft','JustifyCenter','JustifyRight','JustifyBlock'],
                ['RemoveFormat', 'Bold','Italic','Underline','Strike',],
                ['Styles','Format','FontSize', 'TextColor','BGColor'],
                ['Link','Unlink',],
                ['Image', 'Table', 'HorizontalRule' ],
                ['Maximize'],
            ],
        'width': 1000,
        'height': 400,
        'toolbarCanCollapse': True,
        'resize_enabled': True,
        'pasteFromWordRemoveFontStyles': True,
        'visible_filename':True
    }
}

LOCALES = (
    ('ru-RU', u'Русский'),
    ('en', u'English'),
)

LOCALE_PATHS = (
    os.path.join(PROJECT_ROOT, 'locale'),
)

CKEDITOR_UPLOAD_PATH = os.path.join(MEDIA_ROOT, 'uploads')
CKEDITOR_MEDIA_PREFIX = '/media/ckeditor/'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'noreply@webgenesis.ru'
EMAIL_HOST_PASSWORD = 'noreply13'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
EMAIL_SEND_TO = 'anna@webgenesis.ru'


try:
    from dev import *
except:
    pass
