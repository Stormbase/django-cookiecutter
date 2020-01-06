"""
Common settings for testing the application
"""

from .base import *


if not SECRET_KEY:
    SECRET_KEY = "testing"