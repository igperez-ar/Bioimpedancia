# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 09:16:37 2019

@author: Matias
"""

import numpy as np
from abc import ABC

class Circuito(ABC):
    def get_impedancias(self,spectrum):
        pass
    
class Resistencia(Circuito):
    def __init__(self,r):
        self.r=r
    def get_impedancias(self,spectrum):
        return self.r*np.ones(len(spectrum))
        
class Capacitor(Circuito):
    def __init__ (self,c):
        self.c=c        
    def get_impedancias(self,spectrum):        
        return -1j/(2*np.pi*spectrum*self.c)
    
class RCSerie(Circuito):
    def __init__(self,r,c):
        self.r=r
        self.c=c
    def get_impedancias(self,spectrum):
        return self.r-1j/(2*np.pi*spectrum*self.c);
        
class RCParalelo(Circuito):
    def __init__(self,r,c):
        self.r=r
        self.c=c
    def get_impedancias(self,spectrum):  
        Xc=-1j/(2*np.pi*spectrum*self.c)
        return (self.r*Xc)/(self.r+Xc)
        
class RCSerieParalelo(Circuito):
    def __init__(self,r,c,r1):
        self.r=r
        self.c=c
        self.r1=r1
    def get_impedancias(self,spectrum):    
         xc=-1j/(2*np.pi*spectrum*self.c);
         return self.r1+((self.r*xc)/(self.r+xc))   