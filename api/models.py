from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

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
    date = models.DateTimeField(auto_now_add=True, null=True)
    temperature = models.SmallIntegerField(null=True,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(-100)
        ]
    )
    weather_description = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    
    def save(self, *args, **kwargs) -> None:
        self.updated_at = timezone.now()
        return super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return f"{self.date}: {self.temperature} {self.weather_description} - {self.updated_at}"
