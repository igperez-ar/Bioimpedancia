from django.conf import settings
from django.urls import path, include
from django.contrib import admin
from directory.views import HomeView, FileFixerView

urlpatterns = [
    path('',            HomeView.as_view(), name="home"),
    path('simulador/',  HomeView.as_view(), name="simulator"),
    path('reparador-archivos/', FileFixerView.as_view(), name="filefixer"),
]


