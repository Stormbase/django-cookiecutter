from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("{{cookiecutter.project_slug}}.hello.urls")),
    path("admin/", admin.site.urls),
]

# Special url routes for local development. We don't care about coverage here.
if settings.DEBUG:  # pragma: no cover
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
