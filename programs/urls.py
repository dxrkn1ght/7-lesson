from django.urls import path
from . import views


app_name = 'programs'
urlpatterns = [
    path('list/', views.program_list, name='list'),
    path('create/', views.program_add, name='program_add'),
]