from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^multivers/', include('apps.multivers.urls', namespace='multivers')),
    url(r'^grolsch/', include('apps.grolsch.urls', namespace='grolsch')),
    url(r'^mail/', include('apps.mail.urls', namespace='mail')),
    url(r'^flow/', include('apps.flowguard.urls', namespace='flowguard')),
    url(r'^hygiene/', include('apps.hygiene.urls', namespace='hygiene')),
    url(r'^', include('apps.general.urls', namespace='general')),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
