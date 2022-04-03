from django.urls import path
from . import views

app_name = 'manager'

urlpatterns = [
    path('<int:year>/<int:month>/<int:day>/', views.HomeView.as_view(), name='index'),
    path('', views.HomeView.as_view(), name='index'),
    path('update', views.UpdateHomeView.as_view(), name='update'),
    path('week_range', views.UpdateWeekRange.as_view(), name='week_range'),
]