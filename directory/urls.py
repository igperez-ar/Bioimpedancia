from django.conf import settings
from django.urls import path
from django.contrib import admin
from directory.views import HomeView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',            HomeView.as_view(), name="home"),
    # path('simulator/',  HomeView.as_view(), name="simulator"),
    path('file-fixer/', HomeView.as_view(), name="filefixer"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)