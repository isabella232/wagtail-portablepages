from django.urls import path, reverse

from wagtail.admin import widgets as wagtailadmin_widgets
from wagtail.core import hooks

from portablepages.views import export_view, import_view


@hooks.register("register_page_listing_more_buttons")
def page_listing_import_button(
    page, page_perms, is_parent=False, next_url=None
):
    yield wagtailadmin_widgets.Button(
        "Export", reverse("export_page", args=(page.id,)), priority=20
    )
    yield wagtailadmin_widgets.Button(
        "Import", reverse("import_page", args=(page.id,)), priority=20
    )


@hooks.register("register_admin_urls")
def register_portable_page_admin_urls():
    return [
        path("export/<int:page_id>/", export_view, name="export_page"),
        path("import/<int:page_id>/", import_view, name="import_page"),
    ]
