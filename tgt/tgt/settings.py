"""
Django settings for tgt project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
#This is the dynamic path - meaning you should not be hardcoding ANYTHING
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'p&%bn=q1k@n#t3wj8fec67r-h+fuvxy0jz-a*!$ip2fu5*z#1t'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    'BASE_DIR',
)

ALLOWED_HOSTS = []


#templates
#designates templates directory within the tgt directory...NOT (tgt/tgt/templates)... THIS (tgt/templates)
TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates')

#selects the directory for Python to parse templates.
TEMPLATE_DIRS = (
    TEMPLATE_PATH,
)



# Application definition
#Make sure to add any programs you include...for example, we added our base TGTapp and will probably add the app that connects to facebook
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
<<<<<<< HEAD
    'TGTapp',
=======
    'TGTapp'
>>>>>>> ea51b6e5271b05a4e2b124379b23d573ccb244f1
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'tgt.urls'

WSGI_APPLICATION = 'tgt.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
