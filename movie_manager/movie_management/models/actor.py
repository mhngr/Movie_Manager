from django.db import models
from .artist import Artist
from .movie import Movie


class Actor(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('movie', 'artist'),)
