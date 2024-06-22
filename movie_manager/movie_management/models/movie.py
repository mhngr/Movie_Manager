from django.db import models
from .artist import Artist


class Movie(models.Model):
    name = models.CharField(max_length=200)
    production_year = models.IntegerField()
    director = models.ForeignKey(
        Artist, on_delete=models.SET_NULL, related_name="actor_movies", null=True
    )
    actor = models.ManyToManyField(Artist, related_name="director_movies")
