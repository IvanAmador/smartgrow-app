from django.db import models

class Plant(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()