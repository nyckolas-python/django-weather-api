from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from api.serializers import WeatherSerializer
from api.models import Weather
from api.tasks import update_or_create_weather_task, sample_task


# Create your views here.
class WeathersListView(ListAPIView):
    """
        Return list of weather forecast
    """
    permission_classes = (AllowAny,)
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer

class TaskStarterView(APIView):
    """
        Run weather data scraping task and return task id
    """
    def get(self, request, format=None):
        task = update_or_create_weather_task.delay()
        
        return Response(f"The weather data scraping is {task.state}. Task id: {task.id}")
