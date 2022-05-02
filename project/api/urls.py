from django.urls import path

from . import views

appname="api"

urlpatterns = [
    path('', views.DayByDayCommand.as_view({'get':'list'}), name='api'),
    path('total/', views.DayByDayCommandTotal.as_view({'get':'list'}), name='api'),
    path('circuit-total/', views.DayByDayCircuitTotal.as_view({'get':'list'}), name='api'),
    path('circuit-total-total/', views.DayByDayCircuitTotalTotal.as_view({'get':'list'}), name='api'),
    path('comments/', views.AllCommentsOfCustomer.as_view({'get':'list'}), name='api'),
    path('comment-delete/<int:pk>/', views.CommandCommentUpdate.as_view()),
    path('client/<int:pk>/<str:attr>/<str:value>/', views.ClientUpdate.as_view()),
    path('clientfood/<int:pk>/<int:food_id>/<int:value>/', views.ClientDefaultFoodUpdate.as_view()),
    path('commandfood/<int:pk>/<int:food_id>/<int:value>/', views.CommandDefaultFoodUpdate.as_view()),
]
