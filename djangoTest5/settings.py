"""
Django settings for djangoTest5 project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

import socket
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+q*rc^iuzoa(zfymt(yp^^zp-89=kk(r^8*yr68b0qhcjbf&64'

# SECURITY WARNING: don't run with debug turned on in production!

if not "-" in  socket.gethostname()[6:]:
    DEBUG = False
else:
    DEBUG=True


ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djangoTest5',
    'firstApp',
    "haystack"

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'djangoTest5.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = 'djangoTest5.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases


if not "-" in  socket.gethostname()[6:]:

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',  # 数据库引擎
            'NAME': 'cg_log_web',  # 数据库名称
            'USER': 'root',  # 链接数据库的用户名
            'PASSWORD': 'Xhc654477358',  # 链接数据库的密码
            'HOST': '127.0.0.1',  # mysql服务器的域名和ip地址
            'PORT': '3306',  # mysql的一个端口号,默认是3306
        }
    }

else:

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',  # 数据库引擎
            'NAME': 'cg_log_web',  # 数据库名称
            'USER': 'root',  # 链接数据库的用户名
            'PASSWORD': '',  # 链接数据库的密码
            'HOST': '127.0.0.1',  # mysql服务器的域名和ip地址
            'PORT': '3306',  # mysql的一个端口号,默认是3306
        }
    }


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/abc/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]


if not "-" in  socket.gethostname()[6:]:
    SATTIC_ROOT=os.path.join(BASE_DIR, "static")


CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

# haystack serch engine configure
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_cn_backend.WhooshEngine',
        'PATH': os.path.join(BASE_DIR, 'whoosh_index')
    },
}

HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'
