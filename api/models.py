from django.db import models
from django.utils import timezone

# Create your models here.

# class Task(models.Model):
#     SCHEDULED = 'S'
#     PROGRESS = 'P'
#     DONE = 'D'
#     STATUS_CHOICES = [
#         (SCHEDULED, '💡 Scheduled'),
#         (PROGRESS, '🚀 In progress'),
#         (DONE, '✔️ Done'),
#     ]

#     status = models.CharField(
#         max_length=2, choices=STATUS_CHOICES, default=SCHEDULED, null=True)

class Weather(models.Model):
    date = models.DateField(primary_key=True)
    temperature = models.CharField(max_length=5, null=True)
    weather_description = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    
    def save(self, *args, **kwargs) -> None:
        self.updated_at = timezone.now()
        return super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        # return f"Weather forecast for {self.date}: {self.temperature} {self.weather_description} - updated: {self.updated_at.strftime('%d/%m %H:%M')}"
        return f"Weather forecast for {self.date}"
