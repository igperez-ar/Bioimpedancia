import re
from django.shortcuts import render
from django.views.generic import View
from simulador.services import (
   Ad5933,
   Resistencia,
   Capacitor,
   RCSerie,
   RCParalelo,
   RCSerieParalelo)



class IndexView(View):
   
   def get(self, request):
      placa = Ad5933(Resistencia(500))
      placa.simula(100,100,100)

      impedancia_data = placa.get_mod_impedancia_data
      impedancia_data.x = removeWhitespace(impedancia_data.x)    
      return render(request, "simulator.html", {
         'impedancia_data' : impedancia_data,
         'impedancia_data_log':placa.get_mod_impedancia_log_data,
         'fase_data':placa.get_fase_data,
         'cole_cole_data':placa.get_cole_cole_data,
         })

def removeWhitespace(element):
   data = element.split(',')
   return {
      'x':re.sub("\s+", ",", str(data),
      'y':re.sub("\s+", ",", str(data)
      }