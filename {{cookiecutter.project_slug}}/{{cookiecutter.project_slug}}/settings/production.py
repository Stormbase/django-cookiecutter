"""
Place setting overrides for a production environment here.
"""

from .base import *  # noqa

SECURE_HSTS_SECONDS = 31536000  # 1 year
CSRF_COOKIE_SECURE = True
LANGUAGE_COOKIE_SECURE = True

EMAIL_USE_TLS = True
