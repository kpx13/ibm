# -*- coding: utf-8 -*-
from django.db import models

class Photo(models.Model):
    image = models.ImageField(upload_to= 'uploads/gallery', max_length=256, verbose_name=u'картинка')
    order = models.IntegerField(blank=True, default=100, verbose_name=u'порядковый номер')
    
    class Meta:
        verbose_name = u'фотография'
        verbose_name_plural = u'фотографии'
        ordering = ['order']
    
    def __unicode__(self):
        return str(self.id)