from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import APICall
from ..serializers import APICallSerializer


class APICallData(APIView):
    def get(self, request):
        apicalls = APICall.objects.all().order_by('-timestamp')
        serializer = APICallSerializer(apicalls, many=True)
        return Response(serializer.data)
