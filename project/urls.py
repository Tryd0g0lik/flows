"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

"""
project/urls.py
"""
from django.contrib import admin
from wagtail.admin import urls as wagtailadmin_urls
from wagtail import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls
from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny
from django.conf.urls.static import static
from django.views.generic import TemplateView
from project import settings
from project.urls_api import urlpatterns as api_urls
from flow.urls import urlpatterns as flow_urls

schema_view = get_schema_view(
    openapi.Info(
        title="API for test code",
        description="API for test code",
        default_version="1.0.0",
        service_identity=False,
        contact=openapi.Contact(email="work80@mail.ru"),
    ),
    public=True,
    permission_classes=[AllowAny],
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(flow_urls)),
    path("api/", include((api_urls, "api_keys"), namespace="api_keys")),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="swagger"),
    path(
        "swagger<format>/",
        schema_view.without_ui(cache_timeout=0),
        name="swagger-format",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="redoc"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += [
    path("cms/", include(wagtailadmin_urls)),
    path("documents/", include(wagtaildocs_urls)),
    path("pages/", include(wagtail_urls)),
    re_path(
        r"^(?!static/|media/|api/|admin/|redoc/|swagger/).*",
        TemplateView.as_view(template_name="index.html"),
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
