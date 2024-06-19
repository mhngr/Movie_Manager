from ..serializers import ArtistSerializer
from ..models import Artist
from rest_framework.generics import RetrieveAPIView


class ArtistDetail(RetrieveAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer