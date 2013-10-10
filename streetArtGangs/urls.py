from django.conf.urls import patterns, include, url
from django.contrib import admin
from server.views import GangsterViewSet, GangViewSet
from rest_framework.urlpatterns import format_suffix_patterns

admin.autodiscover()



gang_list = GangViewSet.as_view({
    'get': 'list',
})
gang_detail = GangViewSet.as_view({
    'get': 'retrieve',
})

gangster_list = GangsterViewSet.as_view({
    'get': 'list'
})
gangster_detail = GangsterViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = format_suffix_patterns(patterns('server.views',
    url(r'^$', 'api_root'),
    url(r'^gangs/$', gang_list, name='gang-list'),
    url(r'^gangs/(?P<pk>[0-9]+)/$', gang_detail, name='gang-detail'),
    url(r'^gangsters/$', gangster_list, name='gangster-list'),
    url(r'^gangsters/(?P<pk>[0-9]+)/$', gangster_detail, name='gangster-detail')
))
