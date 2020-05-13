import os
from django.core.exceptions import ImproperlyConfigured


# -------------------------{DJANGO SETTINGS}----------------------------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ALLOWED_HOSTS = ['makewiki-cb.herokuapp.com', 'django-testing.dev.habitualhabits.club',
                 'localhost', '127.0.0.1', '0.0.0.0']
SECRET_KEY = os.getenv(
    "SECRET_KEY") or ImproperlyConfigured("SECRET_KEY not set")
DEBUG = False

ROOT_URLCONF = 'makewiki.urls'
WSGI_APPLICATION = 'makewiki.wsgi.application'

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/Los_Angeles'
USE_I18N = True
USE_L10N = True
USE_TZ = True

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.postgres',

    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'compressor',
    'rest_framework',
    'corsheaders',
    'debug_toolbar',
    'imagekit',
    'storages',

    'accounts',
    'wiki',
]


# -------------------------{APP SETTINGS}----------------------------------------------
# wiki app settings
WIKI_PAGE_TITLE_MAX_LENGTH = 600



# -------------------------{AUTH/ACCOUNT SETTINGS}----------------------------------------------
# Where to redirect during authentication
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

DEFAULT_LOGOUT_URL = '/'


AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
)

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators
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



# -------------------------{DATABASE SETTINGS}----------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME':  os.getenv("DB_NAME"),
        'USER':  os.getenv("DB_USER"),
        'PASSWORD': os.getenv("DB_PASSWORD"),
        'HOST': os.getenv("DB_HOST"),
        'PORT': os.getenv("DB_PORT"),
    }
}

# -------------------------{HTML SETTINGS}----------------------------------------------
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO',
                           'https')   # Required for Heroku

# django-cors-headers
# https://github.com/adamchainz/django-cors-headers
CORS_ORIGIN_WHITELIST = [
    "http://localhost:8000",
    "http://127.0.0.1:8000"
]

MIDDLEWARE = [
    #  Caching Middleware
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',

    'corsheaders.middleware.CorsMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
#         'LOCATION': 'make_wiki_cache',
#     }
# }

# djangorestframework
# https://www.django-rest-framework.org/
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAdminUser',
    ]
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    # 'DEFAULT_PERMISSION_CLASSES': [
    #     'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    # ],
}


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
            # Always use forward slashes, even on Windows.
            # Don't forget to use absolute paths, not relative paths.
            os.path.join(BASE_DIR, 'templates').replace('\\', '/'),
        ],
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

# -------------------------{EMAIL SETTINGS}----------------------------------------------
ADMINS = [
    ('Chris', 'christopher.barnes@students.makeschool.com'),
]

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_USE_TLS = True
# EMAIL_PORT = 587
# EMAIL_HOST_USER = os.getenv('EMAIL_ACCOUNT')
# EMAIL_HOST_PASSWORD = os.getenv('EMAIL_PASSWORD')

# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': True,
#     'formatters': {
#         'verbose': {
#             'format': '%(levelname)s [%(asctime)s] %(module)s %(message)s'
#         },
#     },
#     'handlers': {
#         'console': {
#             'level': 'DEBUG',
#             'class': 'logging.StreamHandler',
#             'formatter': 'simple'
#         },
#         'file': {
#             'class': 'logging.handlers.RotatingFileHandler',
#             'formatter': 'verbose',
#             'filename': '/var/www/logs/ibiddjango.log',
#             'maxBytes': 1024000,
#             'backupCount': 3,
#         },
#         'mail_admins': {
#             'level': 'ERROR',
#             'class': 'django.utils.log.AdminEmailHandler'
#         }
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['file', 'console','mail_admins'],
#             'propagate': True,
#             'level': 'DEBUG',
#         },
#     }
# }


# -------------------------{STATIC SETTINGS}----------------------------------------------
# django.contrib.staticfiles
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
# http://whitenoise.evans.io/en/stable/django.html
# USE_S3 = os.getenv('USE_S3', False)

# if USE_S3:
# aws settings
# AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
# AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
# AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
# AWS_DEFAULT_ACL = None
# AWS_S3_CUSTOM_DOMAIN = '%s.s3.us-east-2.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
# AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
# # s3 Static settings
# AWS_STATIC_LOCATION = 'Static'
# STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, AWS_STATIC_LOCATION)
# STATICFILES_STORAGE = 'Habitual_Habits.storage_backends.StaticStorage'
# # s3 public media settings
# AWS_PUBLIC_MEDIA_LOCATION = 'media/public'
# DEFAULT_FILE_STORAGE = 'Habitual_Habits.storage_backends.PublicMediaStorage'
# # s3 private media settings
# AWS_PRIVATE_MEDIA_LOCATION = 'media/private'
# PRIVATE_FILE_STORAGE = 'Habitual_Habits.storage_backends.PrivateMediaStorage'
# else:

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_HOST = os.getenv('DJANGO_STATIC_HOST', '')

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
STATIC_ROOT = os.path.join(BASE_DIR, "static")

STATIC_URL = STATIC_HOST + '/static/'
MEDIA_URL = STATIC_HOST + '/media/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static/assets"),
]

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder'
]


# django-compressor
# https://github.com/django-compressor/django-compressor
COMPRESS_STORAGE = 'compressor.storage.GzipCompressorFileStorage'
COMPRESS_ENABLED = os.getenv('COMPRESS_ENABLED', False)
COMPRESS_OFFLINE = os.getenv('COMPRESS_OFFLINE', False)
COMPRESS_CACHE_BACKEND = "default"

COMPRESS_FILTERS = {
    'css': [
        'compressor.filters.css_default.CssAbsoluteFilter',
        'compressor.filters.cssmin.rCSSMinFilter'
    ],
    'js': [
        'compressor.filters.jsmin.JSMinFilter'
    ]
}

try:
    from makewiki.local_settings import *
except ImportError:
    pass
