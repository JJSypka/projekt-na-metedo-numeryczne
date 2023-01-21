import uklad
import numpy as np
from gauss import Gauss
from uklad import Uklad

class gauss:
    
    def __init__(self, wymiar=5,A=5):
        self.n = wymiar            # maksymalny wymiar macierzy ukladu
        self.u = uklad.Uklad(A)                 # uklad do rozwiazania
        
    def losuj_macierz_A(self):
        A = np.random.random([self.n, self.n])
        return A
    def macierz_trojkątna(self):
        macierz_trojkatna=Gauss.eliminacja(self)
        return macierz_trojkatna
    
    
    
zad = gauss()
print(zad.macierz_trojkątna())