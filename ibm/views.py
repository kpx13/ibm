# -*- coding: utf-8 -*-

from django.core.context_processors import csrf
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import config
from livesettings import config_value
from django.conf import settings

from pages.models import Page
from news.models import Article
from gallery.models import Photo
from links.models import Link
from partners.models import Partner

PAGINATION_COUNT = 10

def get_common_context(request):
    c = {}
    c['lang'] = request.LANGUAGE_CODE
    c['request_url'] = request.path
    c['is_debug'] = settings.DEBUG
    c['links'] = Link.objects.all()
    c['base_partners'] = Partner.objects.filter(is_base=True)
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
    c['recent_news'] = Article.get_list(c['lang'])[:6]
    c['recent_photos'] = Photo.objects.all()[:3]
    c['home_top']     = Page.get('home_top',     c['lang'])['content']
    c['home_history'] = Page.get('home_history', c['lang'])['content']
    return render_to_response('home.html', c, context_instance=RequestContext(request))

def news(request):
    c = get_common_context(request)
    
    items = Article.get_list(c['lang'])
    
    paginator = Paginator(items, PAGINATION_COUNT)
    page = int(request.GET.get('page', '1'))
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        items = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        items = paginator.page(page)
    c['page'] = page
    c['page_range'] = paginator.page_range
    if len(c['page_range']) > 1:
        c['need_pagination'] = True
    c['items'] = items
    
    return render_to_response('news.html', c, context_instance=RequestContext(request))

def news_article(request, slug):
    c = get_common_context(request)
    article = Article.get(slug, c['lang'])
    c['article'] = article
    if request.method == 'POST':
        if request.POST.get('action') == 'comment':
            Article.objects.get(slug=slug).add_comment(request.user, 
                            request.POST.get('content'))
            return HttpResponseRedirect('/news/%s/' % slug)
    return render_to_response('news_item.html', c, context_instance=RequestContext(request))

def gallery(request):
    c = get_common_context(request)
    c['gallery'] = Photo.objects.all()
    return render_to_response('gallery.html', c, context_instance=RequestContext(request))

def partners(request):
    c = get_common_context(request)
    c['partners'] = Partner.objects.all()
    return render_to_response('partners.html', c, context_instance=RequestContext(request))