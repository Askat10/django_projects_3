from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from .models import Cities
from .serializers import CitiesSerializer

@api_view(['GET'])
def get_cities(request: Request):
    queryset = Cities.objects.all()
    serializer = CitiesSerializer(queryset, many=True)
    return Response(serializer.data)