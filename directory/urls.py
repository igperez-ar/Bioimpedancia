from django.conf import settings
from django.urls import path, include
from django.contrib import admin
from directory.views import HomeView, FileFixerView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('',                    HomeView.as_view(),                   name="home"),
    path('reparador-archivos/', csrf_exempt(FileFixerView.as_view()), name="filefixer"),
]
