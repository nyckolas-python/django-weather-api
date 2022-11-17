from rest_framework import serializers
from django_celery_beat.models import CrontabSchedule

from api.models import Weather


class WeatherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Weather
        fields = '__all__'

class ScheduleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CrontabSchedule
        fields = ['hour', 'minute']