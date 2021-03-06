from django.urls import path

from . import views

appname="api"

urlpatterns = [
    path('', views.DayByDayCommand.as_view({'get':'list'})),
    path('total/', views.DayByDayCommandTotal.as_view({'get':'list'})),
    path('circuit-total/', views.DayByDayCircuitTotal.as_view({'get':'list'})),
    path('circuit-total-total/', views.DayByDayCircuitTotalTotal.as_view({'get':'list'})),
    path('comments/', views.AllCommentsOfCustomer.as_view({'get':'list'})),
    path('commentupdate/', views.CommentUpdate.as_view()),
    path('comment-delete/<int:pk>/', views.CommandCommentUpdate.as_view()),
    path('client/', views.ClientUpdate.as_view()),
    path('clientfood/<int:pk>/<int:food_id>/<int:value>/', views.ClientDefaultFoodUpdate.as_view()),
    path('commandfood/<int:pk>/<int:food_id>/<int:value>/', views.CommandDefaultFoodUpdate.as_view()),
    path('commandbymonth/<int:pk>/<int:month>/<int:year>/', views.CommandMoneyMonthUpdate.as_view()),
    path('command/<int:pk>/<int:value>/', views.CommandUpdate.as_view()),
    path('clientcircuit/<int:pk>/<int:circuit>/', views.ClientCircuitUpdate.as_view()),
    path('getclientfood/', views.ClientDefaultFood.as_view({'get':'list'})),
    path('getallclients/', views.GetAllClients.as_view({'get':'list'})),
    # path('getallplanning/', views.GetAllPlanning.as_view({'get':'list'})),
]
