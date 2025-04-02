import os
import socket
import environ
from pathlib import Path
from datetime import timedelta

BASE_DIR = Path(__file__).resolve().parent.parent.parent

env = environ.Env()
environ.Env.read_env(BASE_DIR / ".env")

SECRET_KEY = env("SECRET_KEY", default="chave-insegura")
DEBUG = env.bool("DEBUG", default=True)
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["*"])

try:
    hostname = socket.gethostname()
    ALLOWED_HOSTS.append(hostname)
except:
    pass

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',

    'apps.authentication',
    'apps.users',
    'apps.core',
    'apps.companies',
    'apps.tenants',
]


# SHARED_APPS = [
#     # 'django_tenants',
#     'apps.users',
#     'django.contrib.contenttypes',
#     'django.contrib.auth',
#     'django.contrib.sessions',
#     'django.contrib.admin',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'apps.tenants',
#     'apps.companies',
# ]
#
# TENANT_APPS = [
#     'django.contrib.contenttypes',
#     'django.contrib.auth',
#     'django.contrib.sessions',
#     'django.contrib.admin',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'rest_framework',
#     'apps.authentication',
#     'apps.users',
#     'apps.core',
# ]

# INSTALLED_APPS = SHARED_APPS + [app for app in TENANT_APPS if app not in SHARED_APPS]

MIDDLEWARE = [
    # 'apps.middleware.tenant_from_header.TenantFromHeaderMiddleware',
    # 'apps.middleware.tenant_from_header.TenantFromRequestMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Router de tenants
# DATABASE_ROUTERS = ('django_tenants.routers.TenantSyncRouter',)
# Nome do modelo que representa o tenant (schema)
# TENANT_MODEL = "tenants.TenantCompany"
# TENANT_DOMAIN_MODEL = "tenants.Domain"

# Configuração de banco de dados multi-tenant
DATABASES = {
    'default': {
        # 'ENGINE': 'django_tenants.postgresql_backend',
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('POSTGRES_DB'),
        'USER': env('POSTGRES_USER'),
        'PASSWORD': env('POSTGRES_PASSWORD'),
        'HOST': env('POSTGRES_HOST'),
        'PORT': env('POSTGRES_PORT'),
    }
}

ROOT_URLCONF = 'config.urls'
PUBLIC_SCHEMA_URLCONF = 'config.urls'

STATIC_URL = '/static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Modelo customizado de usuário
AUTH_USER_MODEL = "users.CustomUser"


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "SIGNING_KEY": SECRET_KEY,  # Usa a mesma SECRET_KEY do Django
}

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.IsAuthenticated",
    ),
}
