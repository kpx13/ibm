# -*- coding: utf-8 -*-
from django.contrib import admin
import models

class LinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')

admin.site.register(models.Link, LinkAdmin)