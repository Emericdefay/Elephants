# Django Libs:
from django.urls import path
# Local Libs:
from . import views

app_name = 'manager'

urlpatterns = [
    path('<int:year>/<int:month>/<int:day>/', views.HomeView.as_view(), name='index'),
    path('', views.HomeView.as_view(), name='index'),
    path('update', views.UpdateHomeView.as_view(), name='update'),
    path('week_range', views.UpdateWeekRange.as_view(), name='week_range'),
    path('new_client', views.AddNewClient.as_view(), name='new_client'),
    path('new_food', views.AddNewFood.as_view(), name='new_food'),
    path('new_circuit', views.AddNewCircuit.as_view(), name='new_circuit'),
    path('facture', views.CreateExcel.as_view(), name='facture'),
]
