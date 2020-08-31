"""
Common settings for developing the application

"""

from .base import *  # noqa

try:
    from .local import *  # noqa
except ImportError:
    pass

DEBUG = True

INTERNAL_IPS = ["127.0.0.1"]
