from django.db import models

# Create your models here.

class Blog(models.Model):
    name = models.CharField(max_length=32)
    topic = models.CharField(max_length=60)
    image_link = models.CharField(max_length=255, blank=True)
    post = models.TextField(max_length=2000)