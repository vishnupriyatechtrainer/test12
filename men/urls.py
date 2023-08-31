
from django.urls import path

from . import views

urlpatterns = [

    path('', views.men, name='men'),
    path('watches/', views.watches, name='watches'),
    path('shoes/', views.shoes, name='shoes'),
    
]