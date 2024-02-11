from django.db import models

# Create your models here.
class Shuttle(models.Model):
    name = models.CharField(max_length=20)