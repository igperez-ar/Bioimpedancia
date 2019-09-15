import re
from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from simulador.services import (
   Ad5933,
   Circuito,
   Resistencia,
   Capacitor,
   RCSerie,
   RCParalelo,
   RCSerieParalelo)

# Reemplaza a http://bioimpedancia.untdf.edu.ar/

class IndexView(View):
   
   def get(self, request):
      # Value option group
      circuitoSelec = request.GET.get('circuito')

      # Value circuito
      if (circuitoSelec != None):
         # Carga los valores selecionados
         valueCapacitor = float(request.GET.get('select_capacitor'))
         valueResistencia_1 = int(request.GET.get('select_recistencia_1'))
         valueResistencia_2 = int(request.GET.get('select_recistencia_2'))
      else:
         # Inicializa el simulador default
         valueCapacitor = 10
         valueResistencia_1 = 910
         valueResistencia_2 = 910
         circuitoSelec = 'capacitor'

      # Switch de circuito
      # Construye el circuito con los valores
      def switch(circuitoSelec ,valueCapacitor, valueResistencia_1, valueResistencia_2):
         sw = {
            'capacitor': Capacitor(valueCapacitor),
            'recistencia': Resistencia(valueResistencia_1),
            'serie-rc': RCSerie(
               valueResistencia_1,
               valueCapacitor
               ),
            'paralelo-rc': RCParalelo(
               valueResistencia_1,
               valueCapacitor
               ),
            'serie-paralelo-rc': RCSerieParalelo(
               valueResistencia_1,
               valueCapacitor,
               valueResistencia_2
               ),
         }
         return sw.get(circuitoSelec)

      circuito = switch(circuitoSelec, valueCapacitor, valueResistencia_1, valueResistencia_2)

      placa = Ad5933(circuito)
      placa.simula(100,100,100)

      # Prepara los datos para lo grafico con X e Y
      impedancia_data = formatoGrafico ( placa.get_mod_impedancia_data() )
      impedancia_data_log = formatoGrafico ( placa.get_mod_impedancia_log_data() )
      fase_data = formatoGrafico ( placa.get_fase_data() )
      cole_cole_data = formatoGrafico ( placa.get_cole_cole_data() )

      return render(request, "simulator.html", {
         'impedancia_data' : impedancia_data,
         'impedancia_data_log': impedancia_data_log,
         'fase_data': fase_data,
         'cole_cole_data': cole_cole_data,
      })


def formatoGrafico(elemt):
   # Reemplazar espaciosen blanco por coma
   x = re.sub("\s+", ",", str(elemt['x']))
   y = re.sub("\s+", ",", str(elemt['y']))

   # Eliminar el primar lugar vacio Ej: [,100,200] por [100,200]
   if (x[0:2] == '[,'):
      x = '['+x[2:]

   if (y[0:2] == '[,'):
      y = '['+y[2:]

   #Elimina el punto final del valor Ej: [500.,500.,500.] por [500,500,500]
   x = re.sub("\.,", ",", x)
   y = re.sub("\.,", ",", y)


   return {
      'x':x,
      'y':y
   }