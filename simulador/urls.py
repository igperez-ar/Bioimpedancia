from django.urls import path
from simulador.views import IndexView

urlpatterns = [
   path('simulator/',  IndexView.as_view(), name="simulator"), 
]