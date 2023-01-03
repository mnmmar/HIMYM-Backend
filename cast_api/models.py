from django.db import models

# Create your models here.

class Cast(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    first_episode = models.IntegerField()
    status = models.CharField(max_length=32)
    relationship_status = models.CharField(max_length=32)
    image_link = models.CharField(max_length=2000)