# smartgrow_app/models.py
from django.db import models

class Crop(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()