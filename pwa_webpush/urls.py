from django.conf.urls import url

from .views import manifest, offline, ServiceWorkerView, save_info

# Serve up serviceworker.js and manifest.json at the root
urlpatterns = [
    url('^serviceworker.js$', ServiceWorkerView.as_view(), name='serviceworker'),
    url('^manifest.json$', manifest, name='manifest'),
    url('^offline/$', offline, name='offline'),
    url(r'^webpush/save_information', save_info, name='save_webpush_info'),
]
