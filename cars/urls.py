from django.urls import path
from . import views


app_name = 'cars'
urlpatterns = [
    path('list/', views.car_list, name='list'),
    path('create/', views.car_add, name='car_add'),
]