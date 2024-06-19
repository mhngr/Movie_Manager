from ..serializers import ArtistSerializer
from ..models import Artist
from rest_framework.generics import CreateAPIView


class CreateArtist(CreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
