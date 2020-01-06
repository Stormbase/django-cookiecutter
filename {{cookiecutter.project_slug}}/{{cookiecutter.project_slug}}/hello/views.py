"""
Views for the example app
"""

from django.shortcuts import render


def hello(request):
    """Greets the user with a personal message"""
    user = request.user
    try:
        name = user.get_full_name() or user.username
    except:
        name = "anonymous"

    context = {"name": name}

    return render(request, "example/hello.html", context)
