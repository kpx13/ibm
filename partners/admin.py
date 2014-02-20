# -*- coding: utf-8 -*-
from django.contrib import admin
import models

class PartnerAdmin(admin.ModelAdmin):
    list_display = ('logo', 'name', 'url', 'is_base')

admin.site.register(models.Partner, PartnerAdmin)