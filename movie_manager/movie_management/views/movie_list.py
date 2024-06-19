from ..serializers import MovieSerializer
from ..models import Movie
from rest_framework.generics import ListAPIView


class MovieList(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
