from rest_framework.generics import CreateAPIView
from ..serializers import MovieSerializer
from ..models import Movie


class CreateMovie(CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
