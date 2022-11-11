from django.urls import path
from api import views


urlpatterns = [
    path('v1/forecast/', views.WeathersListView.as_view()),
]