from django.db import models

# Create your models here.

class Timecheckin(models.Model):
    group = models.CharField(max_length=30)
    user = models.CharField(max_length=30)
    timeLate = models.IntegerField()
    day = models.DateField()
    