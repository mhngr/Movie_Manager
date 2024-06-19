from ..serializers import MovieSerializer
from ..models import Movie
from rest_framework.generics import RetrieveAPIView


class MovieDetail(RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    