from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from api.serializers import WeatherSerializer
from api.models import Weather
from api.servises import update_or_create_weather_task


# Create your views here.
class WeathersListView(ListAPIView):
    permission_classes = (AllowAny,)
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer

class TaskStarterView(APIView):
    def get(self, request, format=None):
        update_or_create_weather_task()
        return Response('Data was updated...')
