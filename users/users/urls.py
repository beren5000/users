# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'users.views.home', name='home'),
                       # url(r'^users/', include('users.foo.urls')),
                       # Uncomment the admin/doc line below to enable admin documentation:
                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       url(r'^admin/', include(admin.site.urls)),

                       #third party urls
                       url(r'^oauth2/', include('provider.oauth2.urls', namespace='oauth2')),
)
