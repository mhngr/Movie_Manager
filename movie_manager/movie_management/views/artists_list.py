from ..serializers import ArtistSerializer
from ..models import Artist
from rest_framework.generics import ListAPIView


class ArtistsList(ListAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

    def get_queryset(self):
        data = self.request.GET
        return Artist.objects.filter(role=data["role"])
