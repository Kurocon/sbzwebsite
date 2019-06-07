from django.conf.urls import url

from apps.hygiene import views

urlpatterns = [
    url('^check/$', views.check, name='check'),
    url('^check/(?P<pk>[0-9]+)/$', views.check, name='check_day'),

    url('^plan/$', views.plan, name='plan'),
    url('^plan/(?P<year>[0-9]+)/(?P<month>[0-9]+)/$', views.plan, name='plan_month')
]
