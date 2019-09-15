from django.urls import path
from simulador.views import IndexView

urlpatterns = [
   path('',  IndexView.as_view(), name="simulator"), 
]