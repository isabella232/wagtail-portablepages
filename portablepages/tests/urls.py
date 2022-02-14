from django.urls import include, re_path

from wagtail.admin import urls as wagtailadmin_urls

from portablepages import urls as portablepages_urls

urlpatterns = [
    re_path(r"^admin/", include(wagtailadmin_urls)),
    re_path(r"", include(portablepages_urls)),
]
