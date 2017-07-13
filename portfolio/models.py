from django.db import models

class Project(models.Model):
    name = models.CharField(max_length = 32)
    short_description = models.CharField(max_length = 200)
    long_description = models.TextField()
    
