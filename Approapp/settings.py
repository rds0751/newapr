"""
Django settings for Approapp project.

Generated by 'django-admin startproject' using Django 1.9.13.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$b_l&1(jhv6oiy-s$ah3zu)4or_)5pi)1l!ma#2_@35&tfjcfv'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'loginReg',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # ...
    # `django-fobi` core
    'fobi',

    # `django-fobi` themes
    'fobi.contrib.themes.bootstrap3', # Bootstrap 3 theme
    'fobi.contrib.themes.foundation5', # Foundation 5 theme
    'fobi.contrib.themes.simple', # Simple theme

    # `django-fobi` form elements - fields
    'fobi.contrib.plugins.form_elements.fields.boolean',
    'fobi.contrib.plugins.form_elements.fields.checkbox_select_multiple',
    'fobi.contrib.plugins.form_elements.fields.date',
    'fobi.contrib.plugins.form_elements.fields.date_drop_down',
    'fobi.contrib.plugins.form_elements.fields.datetime',
    'fobi.contrib.plugins.form_elements.fields.decimal',
    'fobi.contrib.plugins.form_elements.fields.email',
    'fobi.contrib.plugins.form_elements.fields.file',
    'fobi.contrib.plugins.form_elements.fields.float',
    'fobi.contrib.plugins.form_elements.fields.hidden',
    'fobi.contrib.plugins.form_elements.fields.input',
    'fobi.contrib.plugins.form_elements.fields.integer',
    'fobi.contrib.plugins.form_elements.fields.ip_address',
    'fobi.contrib.plugins.form_elements.fields.null_boolean',
    'fobi.contrib.plugins.form_elements.fields.password',
    'fobi.contrib.plugins.form_elements.fields.radio',
    'fobi.contrib.plugins.form_elements.fields.regex',
    'fobi.contrib.plugins.form_elements.fields.select',
    'fobi.contrib.plugins.form_elements.fields.select_model_object',
    'fobi.contrib.plugins.form_elements.fields.select_multiple',
    'fobi.contrib.plugins.form_elements.fields.select_multiple_model_objects',
    'fobi.contrib.plugins.form_elements.fields.slug',
    'fobi.contrib.plugins.form_elements.fields.text',
    'fobi.contrib.plugins.form_elements.fields.textarea',
    'fobi.contrib.plugins.form_elements.fields.time',
    'fobi.contrib.plugins.form_elements.fields.url',

    # `django-fobi` form elements - content elements
    'fobi.contrib.plugins.form_elements.test.dummy',
    'easy_thumbnails', # Required by `content_image` plugin
    'fobi.contrib.plugins.form_elements.content.content_image',
    'fobi.contrib.plugins.form_elements.content.content_image_url',
    'fobi.contrib.plugins.form_elements.content.content_text',
    'fobi.contrib.plugins.form_elements.content.content_video',

    # `django-fobi` form handlers
    'fobi.contrib.plugins.form_handlers.db_store',
    'fobi.contrib.plugins.form_handlers.http_repost',
    'fobi.contrib.plugins.form_handlers.mail',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Approapp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'fobi.context_processors.theme',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Approapp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
LOGIN_REDIRECT_URL='/loginReg/profile'
STATIC_ROOT= os.path.join(BASE_DIR,'static/')
