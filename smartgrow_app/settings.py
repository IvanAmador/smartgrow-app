# smartgrow_app/settings.py

import os  

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'smartgrow_app',
]

ROOT_URLCONF = 'smartgrow_app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(BASE_DIR.joinpath('templates'))],  
        'APP_DIRS': True,
        'OPTIONS': {'debug': True},
    },
]

WSGI_APPLICATION = 'smartgrow_app.wsgi.application'