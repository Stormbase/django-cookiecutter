"""
Views for the default hello app
"""

from django.shortcuts import render


def hello(request):
    return render(request, "hello/hello.html")
