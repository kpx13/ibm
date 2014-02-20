# -*- coding: utf-8 -*-
from django.db import models

class Link(models.Model):
    name = models.CharField(max_length=200, blank=True, verbose_name=u'название')
    url = models.CharField(max_length=200, blank=True, verbose_name=u'url сайта')
        
    class Meta:
        verbose_name = u'ссылка'
        verbose_name_plural = u'ссылки'
        ordering=['id']
        
    def __unicode__(self):
        return str(self.id)
    
