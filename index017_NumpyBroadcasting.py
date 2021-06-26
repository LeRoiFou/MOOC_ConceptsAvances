"""
En numpy il y a 4 notions fondamentales à maîtriser :
-> Ndarray : tableau numpy
-> Indexation avancée
-> Vectorisation
-> Broadcasting

Le broadcasting permet de faire des calculs entre plusieurs
tableaux numpy de dimensions différentes

Cependant :
-> Lorsqu'on a des tableaux qui dépassent 2 dimensions, il est difficile
de savoir ce que fait le broadcasting
-> Le broadcasting peut présenter des tableaux de très grande dimension
et peut poser problème en terme de mémoires

Éditeur : Laurent REYNAUD
Date : 25-06-2021
"""

import numpy as np

"Calcul entre deux tableaux de même dimensions"
a = np.array([1, 2, 3])
b = np.array([5, 5, 5])
print(a*b)

"Calcul entre deux tableaux de dimension différente"
c = np.array([5])
print(a*c)

"Calcul entre un tableau à 1 dimension et un entier"
print(a * 5)
