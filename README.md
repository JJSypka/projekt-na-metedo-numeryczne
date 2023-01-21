# projekt-na-metedo-numeryczne
Rozwiązywanie układów równań Ax = B za pomocą macierzy odwrotnej i metody Cholesky'ego. Metoda polega na rozkładzie macierzy A na iloczyn D ·G, obliczeniu macierzy odwrotnej A−1 za pomocą podanego iloczynu i na koniec obliczeniu x ze wzoru A−1 ·B. W tym miejscu warto dodać, że macierzą odwrotną do macierzy dolnie-trójkątnej jest macierz dolnie-trójkątna, a macierzą odwrotną do macierzy górnie-trójkątnej jest macierz górnie-trójkątna. Porównanie tej metody z dwoma innymi metodami rozwiązywania układów równań

1. Losowanie macierzy A i B
2. Rozklad macierzy A na D*G (teraz L*U)
3. Wyznaczyć macierze odwrotne do D i G
4. Wyznaczyć A^(-1)=D^(-1)* G^(-1)
5. Wyznaczyc X=A^(-1)*B
6. Porównać tą metedę do 2 innych np. Gauss i Gauss-Jordan
7. Napisać raport