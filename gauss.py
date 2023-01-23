import numpy as np


class Gauss:
    
    def __init__(self, wymiar = 3 ,A = 3):
        self.n = wymiar            # maksymalny wymiar macierzy ukladu               # uklad do rozwiazania
        self.X = np.zeros([self.n, 1])               # wektor rozwiazania
        
    def losuj_macierz_A(self, n = 3):
        A = np.random.random([self.n, self.n])
        return A
    
    def macierz_trojkątna(self,n = 3):
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
        
        
zad = Gauss()
print(zad.losuj_macierz_A())
print("")
print(zad.macierz_trojkątna())
zad.rozwiaz_trojkatny()
print("")
print(zad.wypisz_rozwiazanie())

# pytania:
# 1. Czy okay, ze losuje takie macierze?
# 2. czy na tym to polega? 
# 3. czy dobrze klasa zadanie?
# 4. Czy moge porownac do metody Choleskyieg( bo zgrzyt ze te metody dzialaja w podobny sposob)? Bo rozwiazania zawsze sa z zerami itp i czy da sie jakos je wylosowac z lepszymi liczbami?
