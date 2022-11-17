from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_202_ACCEPTED, HTTP_400_BAD_REQUEST, HTTP_200_OK
from django_celery_beat.models import CrontabSchedule, PeriodicTask

from api.serializers import WeatherSerializer, ScheduleSerializer
from api.models import Weather
from api.tasks import update_or_create_weather_task, sample_task


# Create your views here.
class WeathersListView(ListAPIView):
    """
        Return list of weather forecast
    """
    permission_classes = (AllowAny,)
    queryset = Weather.objects.all().order_by('-updated_at')
    serializer_class = WeatherSerializer

class TaskStarterView(APIView):
    """
        Run weather data scraping task and return task id
    """
    def get(self, request, format=None):
        task = update_or_create_weather_task.delay()
        
        return Response(f"Task id: {task.id}, state: {task.state}.")

class TaskSchedulerView(APIView):
    """
        Schedule time (hour, minute) for daily task.
    """
    
    def get(self, request, format=None):
        schedule, _ = CrontabSchedule.objects.get_or_create(hour=9, minute=0)
        task = PeriodicTask.objects.filter(name="run_scraping_every_day").first()

  
        return Response({
                        "task_name": f"{task.name}",
                        "hour": f"{task.crontab.hour}",
                        "minute": f"{task.crontab.minute}"
                    },
                    status=HTTP_200_OK)
    
    def put(self, request, format=None):
        serializer = ScheduleSerializer(data=request.data)
        if serializer.is_valid():
            hour = serializer.data.get("hour", None)
            minute = serializer.data["minute"]
            try:
                schedule, _ = CrontabSchedule.objects.get_or_create(hour=hour, minute=minute)
                task = PeriodicTask.objects.filter(name="run_scraping_every_day").update(
                    crontab=schedule,
                    enabled=True,
                    )
            except Exception as e:
                return Response(e, status=HTTP_400_BAD_REQUEST)

            return Response(
                    {
                        "hour": f"{hour}",
                        "minute": f"{minute}"
                    },
                    status=HTTP_202_ACCEPTED
            )

        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

