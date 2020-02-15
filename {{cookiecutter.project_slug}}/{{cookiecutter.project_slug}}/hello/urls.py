"""
Url patterns for the hello app
"""

from django.urls import path

from .views import hello

urlpatterns = [path("", hello, name="hello")]
