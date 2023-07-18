from django.urls import path
from . import views

urlpatterns = [
    path('home-menu/', views.Home_Menu),
]