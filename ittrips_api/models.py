from django.db import models

# Create your models here.
class Trip(models.Model):
    name = models.CharField(max_length=32)
    duration = models.CharField(max_length=32)
    overview = models.CharField(max_length=300)
    activities = models.CharField(max_length=500)