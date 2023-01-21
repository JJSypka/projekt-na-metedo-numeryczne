"""Klasa przechowujaca uklad rownan i udostepniajaca uzyteczne metody"""

import numpy as np

class Uklad:
      
    def losuj_uklad(self):
        """Losowanie ukladu"""
        A = np.random.random([self.n, self.n])
        B = np.random.random([self.n, 1])
        return A