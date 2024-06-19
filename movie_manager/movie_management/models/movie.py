from django.db import models


class Movie(models.Model):
    DoesNotExist = None
    objects = None
    name = models.CharField(max_length=200)
    production_year = models.IntegerField()

