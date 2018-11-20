import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = 's$g^n1!&9wg(2^m)ls1&8#vgl3z3_48qb-fi08l&ey&w4$d5kp'
DEBUG = False
ALLOWED_HOSTS = [
    '127.0.0.1',
    'klon.ap-northeast-1.elasticbeanstalk.com',
    'd2lsr90acgtyop.cloudfront.net',
    'klongroup.com'
]

INSTALLED_APPS = [
    'home.apps.HomeConfig',
    'api.apps.ApiConfig',

    'django_filters',
    'rest_framework',
    'storages',
    'multiselectfield',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'klon.urls'

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
                'django.contrib.messages.context_processors.messages'
            ],
        },
    },
]

WSGI_APPLICATION = 'klon.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'klon',
        'USER': 'klon',
        'PASSWORD': '68YSehZhc8Ph8Pd',
        'HOST': 'klon.cd8iujepsg4q.ap-northeast-1.rds.amazonaws.com',
        'PORT': '5432',
    }
}

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

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 10
}

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
)

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Tokyo'
USE_I18N = True
USE_L10N = True
USE_TZ = True

CSRF_COOKIE_SECURE = True
CSRF_USE_SESSIONS = True

CORS_ORIGIN_WHITELIST = 'localhost:8000',

AWS_S3_OBJECT_PARAMETERS = {
'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
'CacheControl': 'max-age=94608000',
}

AWS_S3_HOST = "s3-ap-northeast-1.amazonaws.com"
AWS_STORAGE_BUCKET_NAME = 'klons3'
AWS_CLOUDFRONT_DOMAIN = 'd2ec47gai1sijw.cloudfront.net'
AWS_S3_REGION_NAME = 'us-west-2'
AWS_ACCESS_KEY_ID = 'AKIAISP2GY73LRP5AXFQ'
AWS_SECRET_ACCESS_KEY = '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'

AWS_S3_CUSTOM_DOMAIN = 'd2ec47gai1sijw.cloudfront.net'
AWS_S3_FILE_OVERWRITE = False

MEDIAFILES_LOCATION = 'media'
MEDIA_ROOT = '/%s/' % MEDIAFILES_LOCATION
MEDIA_URL = '//%s/%s/' % (AWS_CLOUDFRONT_DOMAIN, MEDIAFILES_LOCATION)
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'

STATICFILES_LOCATION = 'static'
STATIC_ROOT = '/%s/' % STATICFILES_LOCATION
STATIC_URL = '//%s/%s/' % (AWS_CLOUDFRONT_DOMAIN, STATICFILES_LOCATION)
STATICFILES_STORAGE = 'custom_storages.StaticStorage'

AWS_DEFAULT_ACL = None