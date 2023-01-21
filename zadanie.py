import numpy as np
import scipy
import scipy.linalg

# #1. Losowanie macierzy A i B
# 2. Rozklad macierzy A na D*G (teraz L*U)
# 3. Wyznaczyć macierze odwrotne do D i G
# 4. Wyznaczyć A^(-1)=D^(-1)* G^(-1)
# 5. Wyznaczyc X=A^(-1)*B
class zadanie:
    def __init__(self, wymiar=5):
        self.n = wymiar            # maksymalny wymiar macierzy ukladu
        
    def losuj_macierz_A(self):
        A = np.random.random([self.n, self.n])
        return A
    
    def losuj_macierz_B(self):
        B = np.random.random([self.n, 1])
        return B
    
    def rozkład_A_na_L(self):
        macierz_A=self.losuj_macierz_A()
        P,L,U=scipy.linalg.lu(macierz_A)
        return L
    
    def rozkład_A_na_U(self):
        macierz_A=self.losuj_macierz_A()
        P,L,U=scipy.linalg.lu(macierz_A)
        return U
    
    def macierz_odwrotna_do_L(self):
        macierz_L= self.rozkład_A_na_L()
        macierz_odwrotna_do_L=np.linalg.inv(macierz_L)
        return macierz_odwrotna_do_L
        
    
    def macierz_odwrotna_do_U(self):
        macierz_U= self.rozkład_A_na_U()
        macierz_odwrotna_do_U=np.linalg.inv(macierz_U)
        return macierz_odwrotna_do_U
    
    def oblicz_macierz_odwrotna_do_A(self):
        macierz_1=self.macierz_odwrotna_do_L()
        macierz_2=self.macierz_odwrotna_do_U()
        macierz_odwrotna_A=macierz_1 * macierz_2
        return macierz_odwrotna_A
    
    def wyznacz_macierz_x(self):
        macierz_1= self.oblicz_macierz_odwrotna_do_A()
        macierz_2=self.losuj_macierz_B()
        macierz_x=macierz_1 * macierz_2
        return macierz_x
        
        
zad = zadanie()
print(zad.wyznacz_macierz_x())