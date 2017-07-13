# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Contains databse information
# Create your models here.

class Language(models.Model):


    name = models.CharField(max_length = 32)

    def __str__(self):
        return self.name

class Technology(models.Model):
    class Meta:
        verbose_name_plural = 'technologies'

    name = models.CharField(max_length = 32)
    description = models.TextField()

    language = models.ForeignKey(Language)

    def __str__(self):
        return self.name
