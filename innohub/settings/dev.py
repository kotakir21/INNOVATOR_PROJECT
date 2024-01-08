from .base import *  # noqa

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "h3x^rax8qirex48&2rx4udk#gj5j1apc&k8a74_bf7nn76=r%4"

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

CSRF_TRUSTED_ORIGINS = ['https://8000-round-river-24676714.eu-ws2.runcode.io',]

INSTALLED_APPS += [  # noqa
    "django_sass",
]

#EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'kbobroberts@gmail.com'
EMAIL_HOST_PASSWORD = 'mjrf xpyc snum bvak'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


WAGTAIL_CACHE = False

try:
    from .local import *  # noqa
except ImportError:
    pass
