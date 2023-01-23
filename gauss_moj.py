import uklad
import numpy as np
from gauss import Gauss
from uklad import Uklad

class gauss:
    
    def __init__(self, wymiar=10,A=10):
        self.n = wymiar            # maksymalny wymiar macierzy ukladu
        self.u = uklad.Uklad(A)                 # uklad do rozwiazania
        self.X = np.zeros([self.n, 1])               # wektor rozwiazania
        
    def losuj_macierz_A(self, n=10):
        A = np.random.random([self.n, self.n])
        return A
    
    def macierz_trojkątna(self,n=10):
        #macierz_trojkatna=Gauss.eliminacja(self)
        #return macierz_trojkatna
        macierz= self.losuj_macierz_A()

        # Applying Gauss Elimination
        for i in range(n):
            if macierz[i][i] == 0.0:
                return('Divide by zero detected!')
            else:
                   for j in range(i+1,n):
                    ratio = macierz[j][i]/macierz[i][i]
                
                    for k in range(n):
                        macierz[j][k] = macierz[j][k] - ratio * macierz[i][k]
        return macierz
        
        
    def rozwiaz_trojkatny(self):
        """Metoda rozwiazujaca uklad trojkatny gorny"""
        for i in range(self.n - 1, -1, -1):
            macierz = self.macierz_trojkątna()
            suma = macierz[i, 0]
            for j in range(i + 1, self.n):
                suma -= macierz[i, j] * self.X[j, 0]
            self.X[i, 0] = suma / macierz[i, i]
            
    def wypisz_rozwiazanie(self):
        """Metoda wyswietlajaca wektor rozwiazania"""
        print(f"Wektor rozwiazania: {self.X[:, 0]}")
zad = gauss()
print(zad.losuj_macierz_A())
print("")
print(zad.macierz_trojkątna())
zad.rozwiaz_trojkatny()
print("")
print(zad.wypisz_rozwiazanie())