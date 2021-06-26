"""
En numpy il y a 4 notions fondamentales à maîtriser :
-> Ndarray : tableau numpy
-> Indexation avancée
-> Vectorisation
-> Broadcasting

Ndarray est un tableau numpy contenant des éléments de même type qui
offre l'avantage de recourir à des fonctions très spécialisées pour un 
type donné
(Ndarray = n-dimension array = tableau à n dimension)

Le tableau numpy ne doit avoir qu'un seul type d'élément.
La liste des éléments que peut conteneur ce tableau peut être effectué
avec l'instruction : print(np.sctypes)

Tout comme les listes, les tableaux numpy sont mutables mais on ne
peut pas ajouter d'éléments dans ce tableau (contrairement à 
la fonction native 'append' pour les listes)


"""

import numpy as np

# Types disponibles
print("\n Types disponibles pour les tableaux numpy :")
print(np.sctypes)

# Création d'un tableau à une dimension avec 3 éléments
print("\nTableau à 1 dimension :")
tab1 = np.ones(shape=3)
print(tab1)

# Création d'un tableau à deux dimensions avec deux éléments
# en recourant à un tuble
print("\nTableau à 2 dimensions :")
tab2 = np.ones(shape=(2, 2))
print(tab2)

# Modification de la valeur au composant 1, 1
tab2[1, 1] = 18
print(tab2)
