from django.db import models

# Create your models here


class Project(models.Model):
    title = models.CharField()
    description = models.TextField()
    image = models.models.ImageField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
