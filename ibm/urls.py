# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.shortcuts import redirect
admin.autodiscover()

import settings
import views

urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    url(r'^favicon\.ico$', redirect, {'url': '/static/favicon.ico'}),

    url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/jsi18n/', 'django.views.i18n.javascript_catalog'),
    url(r'^settings/', include('livesettings.urls')),
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')),

    url(r'^$', views.home),
    url(r'^news/$', views.news),
    url(r'^news/(?P<slug>[\w-]+)/$' , views.news_article),
    url(r'^gallery/$', views.gallery),
    url(r'^partners/$', views.partners),
    url(r'^(?P<page_name>[\w-]+)/$' , views.page),
    url(r'^links' , views.all_urls_view),

)

