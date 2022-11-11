from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from api.serializers import WeatherSerializer
from api.models import Weather


# Create your views here.
class WeathersListView(ListAPIView):
    permission_classes = (AllowAny,)
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer
