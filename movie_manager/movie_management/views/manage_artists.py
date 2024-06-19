from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..models import Movie, Artist, Director, Actor


class ManageDirectors(APIView):
    def post(self, request, movie_id, artist_id):
        try:
            movie = Movie.objects.get(pk=movie_id)
            artist = Artist.objects.get(pk=artist_id)
            Director.objects.create(movie=movie, artist=artist)
            return Response(status=status.HTTP_200_OK)
        except (Movie.DoesNotExist, Artist.DoesNotExist):
            return Response(status=status.HTTP_404_NOT_FOUND)


class ManageActors(APIView):
    def post(self, request, movie_id, artist_id):
        try:
            movie = Movie.objects.get(pk=movie_id)
            artist = Artist.objects.get(pk=artist_id)
            Director.objects.create(movie=movie, artist=artist)
            return Response(status=status.HTTP_200_OK)
        except (Movie.DoesNotExist, Artist.DoesNotExist):
            return Response(status=status.HTTP_404_NOT_FOUND)

