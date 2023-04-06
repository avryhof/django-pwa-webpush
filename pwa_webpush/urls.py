from django.urls import path
from django.utils import timezone
from django.views.decorators.cache import cache_page
from django.views.i18n import JavaScriptCatalog

from .views import manifest, offline, ServiceWorkerView, save_info

# When we last restarted the server; used for cache control headers and
# invalidating the server side cache on server restart
last_modified_date = timezone.now().strftime("%Y-%m-%d_%H:%M:%S")

# Serve up serviceworker.js and manifest.json at the root
urlpatterns = [
    path(
        "jsi18n/",
        cache_page(86400, key_prefix="js18n-%s" % last_modified_date)(JavaScriptCatalog.as_view(packages=["webpush"])),
        name="javascript-catalog",
    ),
    path("save_information", save_info, name="save_webpush_info"),
    path("serviceworker.js", ServiceWorkerView.as_view(), name="serviceworker"),
    path("manifest.json", manifest, name="manifest"),
    path("offline/", offline, name="offline"),
    path("webpush/save_information", save_info, name="save_webpush_info"),
]
