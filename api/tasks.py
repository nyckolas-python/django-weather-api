import os

from celery import shared_task
from celery.utils.log import get_task_logger
from time import sleep

from api.models import Weather
from api.servises import _scrap_weather_info


logger = get_task_logger(__name__)

@shared_task
def sample_task():
    print("The sample task just ran.")
    sleep(5)
    
    logger.info("The sample task just ran.")
    return None

@shared_task(bind=True)
def update_or_create_weather_task(self):
    forecast_json = _scrap_weather_info()
    for day, data in enumerate(forecast_json):
        self.update_state(state='PROGRESS',
                meta={'current day': day, 'total': len(forecast_json)})
        instance, created = Weather.objects.update_or_create(date=data['date'], defaults=data)
        if instance:
            self.update_state(state='Done',
                meta={'total': len(forecast_json)})
        if created:
            print(f"\n{instance}\nWas created")
        else:
            print(f"\n{instance}\nWas updated")
    return True
