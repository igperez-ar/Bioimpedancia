# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 09:16:37 2019

@author: Matias
"""
import re
import numpy as np
from .circuito import Circuito
 

class Ad5933():
    def __init__(self,circuito: Circuito):
        self.circuito=circuito

    def simula(self,init_freg,delta,inc):
        self.spectrum=np.array(list(range(init_freg,init_freg+delta*inc+inc,inc)))
        self.z=self.circuito.get_impedancias(self.spectrum)

    def _check_sim(self):
        try:
            self.spectrum
            return True
        except AttributeError:
            return False

    def get_mod_impedancia_data(self): 
        return {
            'x':self.spectrum,
            'y':np.abs(self.z)
        }       

    def get_mod_impedancia_log_data(self):
        return {
            'x':np.log10(self.spectrum),
            'y':np.abs(self.z)
        }
   
    def get_fase_data(self):
        return {
            'x':self.spectrum,
            'y':np.angle(self.z)*180/np.pi
            }

    def get_cole_cole_data(self):
        return {
            'x':np.real(self.z[2:]),
            'y':-np.imag(self.z[2:])
            }
       
        
