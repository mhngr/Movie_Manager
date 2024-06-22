from rest_framework.generics import DestroyAPIView
from ..models import Movie


class DeleteMovie(DestroyAPIView):
    def get_object(self, *args, **kwargs):
        id = self.kwargs['id']
        return Movie.objects.get(id=id)
