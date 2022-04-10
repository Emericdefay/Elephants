from django.urls import path

from . import views

appname="api"

urlpatterns = [
    path('', views.DayByDayCommand.as_view({'get':'list'}), name='api'),
]
