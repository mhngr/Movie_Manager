from django.db import models
from django.db.models import CASCADE

from .artist import Artist


class Movie(models.Model):
    name = models.CharField(max_length=100)
    production_year = models.DecimalField()
    director = models.ForeignKey(Artist, on_delete=CASCADE, null=True, blank=True)
    actor = models.ManyToManyField(Artist, on_delete=CASCADE, null=True, blank=True)
