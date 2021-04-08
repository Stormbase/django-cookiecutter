"""
Place setting overrides for a production environment here.
"""
import environ
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
from sentry_sdk.integrations.logging import ignore_logger

from .base import *  # noqa

env = environ.Env()


# Initialize Sentry SDK
if SENTRY_DSN:
    sentry_sdk.init(
        dsn=SENTRY_DSN,
        environment=env.str("SENTRY_ENVIRONMENT", default=None),
        traces_sample_rate=env.float("SENTRY_TRACES_SAMPLE_RATE", default=0),
        send_default_pii=True,
        integrations=[DjangoIntegration()],
    )
    # Ignore disallowed hosts
    ignore_logger("django.security.DisallowedHost")

# Set CONN_MAX_AGE for database connection pooling explicitly
CONN_MAX_AGE = env.int("DB_CONN_MAX_AGE", default=None)
if CONN_MAX_AGE:
    DATABASES["default"]["CONN_MAX_AGE"] = CONN_MAX_AGE

# Storage configuration
DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

AWS_S3_REGION_NAME = env.str("AWS_S3_REGION_NAME", default="eu-central-1")
AWS_S3_ENDPOINT_URL = env.url("AWS_S3_ENDPOINT_URL", default=None)
AWS_ACCESS_KEY_ID = env.str("AWS_ACCESS_KEY_ID", default=None)
AWS_SECRET_ACCESS_KEY = env.str("AWS_SECRET_ACCESS_KEY", default=None)
AWS_STORAGE_BUCKET_NAME = env.str("AWS_STORAGE_BUCKET_NAME", default=None)
AWS_DEFAULT_ACL = "public-read"
AWS_S3_CUSTOM_DOMAIN = env.str(
    "AWS_S3_CUSTOM_DOMAIN",
    default="{}.s3.amazonaws.com".format(AWS_STORAGE_BUCKET_NAME),
)
AWS_S3_MAX_MEMORY_SIZE = 20480  # 20mb max before temp files are used
AWS_S3_OBJECT_PARAMETERS = {
    "CacheControl": env.str(
        "AWS_S3_CACHECONTROL", default="max-age=2592000"
    ),  # Cache for 30 days by default
}

# HTTPS redirect
SECURE_SSL_REDIRECT = env.bool("SECURE_SSL_REDIRECT", default=True)

# https://docs.djangoproject.com/en/3.2/ref/settings/#secure-hsts-seconds
# https://docs.djangoproject.com/en/3.2/ref/settings/#secure-hsts-include-subdomains
# https://docs.djangoproject.com/en/3.2/ref/settings/#secure-hsts-preload
# FIXME: [before-launch-checklist] Enable HSTS support
SECURE_HSTS_SECONDS = 0  # Remove this when going live
# SECURE_HSTS_SECONDS = 63072000  # 2 years

SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # Has no effect when SECURE_HSTS_SECONDS is 0
SECURE_HSTS_PRELOAD = True  # Has no effect when SECURE_HSTS_SECONDS is 0

SECURE_REFERRER_POLICY = "same-origin"

# Only send cookies over https when we can assume https is enabled
SESSION_COOKIE_SECURE = SECURE_SSL_REDIRECT
CSRF_COOKIE_SECURE = SECURE_SSL_REDIRECT
LANGUAGE_COOKIE_SECURE = SECURE_SSL_REDIRECT

EMAIL_USE_TLS = True

STATIC_ROOT = "/public/static"
