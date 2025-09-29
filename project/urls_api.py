from django.urls import path, include
from flow.urls_api import urlpatterns as flow_api_urls

urlpatterns = [
    path("page/", include(flow_api_urls)),  #  "api_content_keys")
]
