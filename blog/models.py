# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Post(models.Model):
    # name = models.FieldReferenceType(restrictions)
    title = models.CharField(max_length = 140)
    body = models.TextField()
    date = models.DateTimeField()

    # this is a metadata parsing method
    def __str__(self):
        return self.title
