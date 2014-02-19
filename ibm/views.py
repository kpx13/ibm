# -*- coding: utf-8 -*-

from django.core.context_processors import csrf
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User
import config
from livesettings import config_value
from django.conf import settings

from pages.models import Page

PAGINATION_COUNT = 5

def get_common_context(request):
    c = {}
    c['lang'] = request.LANGUAGE_CODE
    c['request_url'] = request.path
    c['is_debug'] = settings.DEBUG
    c['field_1'] = config_value('MyApp', 'field_1')
    c['field_2'] = config_value('MyApp', 'field_2')
    c['field_3'] = config_value('MyApp', 'field_3')
    c['field_4'] = config_value('MyApp', 'field_4')
    
    c.update(csrf(request))
    return c

def page(request, page_name):
    c = get_common_context(request)
    p = Page.get(page_name, request.LANGUAGE_CODE)
    
    if p:
        c.update({'p': p})
        return render_to_response('page.html', c, context_instance=RequestContext(request))
    else:
        raise Http404()

def home(request):
    c = get_common_context(request)
    c['request_url'] = 'home'
    #c['content'] = Page.get('home', c['lang'])['content']
    return render_to_response('home.html', c, context_instance=RequestContext(request))

def about(request):
    c = get_common_context(request)
    c['content'] = Page.get('about', c['lang'])['content']
    return render_to_response('about.html', c, context_instance=RequestContext(request))

def services(request):
    c = get_common_context(request)
    c['left'] = Page.get('servicesleft', c['lang'])['content']
    c['right'] = Page.get('servicesright', c['lang'])['content']
    return render_to_response('services.html', c, context_instance=RequestContext(request))