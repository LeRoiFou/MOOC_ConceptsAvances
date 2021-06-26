"""
En numpy il y a 4 notions fondamentales à maîtriser :
-> Ndarray : tableau numpy
-> Indexation avancée : voir exemples ci-dessous
-> Vectorisation
-> Broadcasting

Éditeur : Laurent REYNAUD
Date : 25-06-2021
"""

import numpy as np

# Tableau avec 3 linges et 3 colonnes avec des entiers de 1 à 10
tab1 = np.random.randint(1, 10, size=(3, 3))
print(f"\n{tab1}")


"Slicing lignes / colonnes"

print(f"`\n{tab1[1:, 2:]}")


"Modification de la dimension du tableau numpy"

tab2 = np.random.randint(1, 10, size=(4, 4))
print(f"\n{tab2}")
tab3 = tab2.reshape(8, 2)
print(f"\n{tab3}")


"Manipulation du tableau numpy"

# Tableau des t° du mois de mars (données au hasard)
mars = np.random.randint(-5, 20, size=31)
print(f"\n{mars}")

# Températures >= 0 °C : résultat sous la forme d'un tableau de boléen
tempere = mars >= 0
print(f"\n{tempere}")

# Combien de jours du mois de mars il a fait une température >= 0 °C ?
result1 = np.sum(mars>=0)
print(f"\nNombre de jours >= à 0 °C au mois de mars : {result1}")

# Combien de jour il a fait 20 °C au mois de mars ?
result2 = np.any(mars==20)
print(f"\n{result2}")

# Est-ce que tous les jours du mois de mars il a fait une t° > 20 °C ?
result3 = np.all(mars>0)
print(f"\n{result3}")


"Combinaison de tableaux numpy"

jour_mars = np.arange(1, mars.size + 1, dtype=np.int8)
print(f"\n{jour_mars}")

# Nombre de jours où il a fait + 10 °C au cours de la 2ème quinzaine de mars
result4 = np.sum((mars>10) & (jour_mars>=15))
print(f"\nNombre de jours > 10 °C 2ème quinzaine de mars : {result4}")


"Sous-ensembles de tableaux"

# Nouveau tableau avec des températures > 10 °C
tab4 = mars[mars>10]
print(f"\n{tab4}")

# Remplacement des t° < 0 par la moyenne des t° positives
moy = np.mean(mars[mars>0])
mars[mars<0] = moy
print(f"\n{mars}")
