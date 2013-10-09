from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns
from server import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^gangs/$', views.GangList.as_view()),
    url(r'^gangs/(?P<pk>[0-9]+)/$', views.GangDetail.as_view()),
    url(r'^gangsters/$', views.GangsterList.as_view()),
    url(r'^gangsters/(?P<pk>[0-9]+)/$', views.GangsterDetail.as_view()),
)


urlpatterns = format_suffix_patterns(urlpatterns)
