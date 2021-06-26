"""
Librairie pandas

Notions de la librairie pandas :
Tableau à 1 dimension (1 colonne) = Series
Tableau à 2 dimensions (2 colonnes) = DataFrame
index : en-têtes des lignes

L'avantage de cette librairie est que les opérations ne
se feront entre deux tableaux qui auront deux index identiques
À titre d'exemple deux tableaux avec un en-tête noms, prenoms et âges :
Les additions ne se feront que pour les colonnes qui auront le label 'ages'

Autre avantage : la librairie pandas permet d'afficher les en-têtes des
tableaux qui ne sont pas par principe, créés par le programmeur concepteur.
À cela, les données sont généralement importés d'un fichier html, csv,
excel, json, sql, python pickle...

Les séries sont des tableaux à 1 dimension sur lesquels on va mettre un
index au niveau des lignes uniquement

Éditeur : Laurent REYNAUD
Date : 25-06-2021
"""

import pandas as pd

# Tableau d'âge de personnes
s = pd.Series([20, 30, 40, 50],
              index=['eve', 'bill', 'liz', 'bob'])
print("\nTableau d'âge de personnes")
print(s)

# Liste des valeurs du tableau numpy
print("\nListe des valeurs du tableau numpy")
print(s.values)

# Liste des index du tableau
print("\nListe des index du tableau")
print(s.index)

# Accéder aux éléments du tableau
print("\nAge de 'eve'")
print(s.loc['eve'])

# Accéder aux valeurs de Eve jusqu'à Liz (Attention inclus)
print("\nAccéder aux valeurs de 'eve' jusqu'à 'liz'")
print(s.loc['eve':'liz'])

# Tableaux d'animaux détenus selon des personnes listés
animaux = ['chien', 'chat', 'chat', 'chien', 'poisson']
proprio = ['eve', 'bob', 'eve', 'bill', 'liz']

# Combinaison des 2 tableaux ci-avant
s = pd.Series(animaux, 
              index=proprio)
print("\nCombinaison des tableaux 'animaux' et 'proprio'")
print(s)

# Slicing sur ce nouveau tableau
# print(s.loc['eve':'liz'])
"""Résultat : il n'est pas possible de faire des slicings
sur des index dupliqués...
Solution : trier d'abord les index"""

# Trie des index
s = s.sort_index()
print('\nTrie des index')
print(s.loc['eve':'liz'])

# La fonction iloc permet d'accéder aux éléments du tableau
print("\nAccès au 1er élément de la liste")
print(s.iloc[0])
print("\nAccès au 5ème élément de la liste")
print(s.iloc[4])

# Accès aux index et aux valeurs de l'élément 1 à 2 (élément 3 exclu)
print("\nAccès aux index et aux valeurs de l'élément 1 à 2")
print(s.iloc[1:3])

# Tous les index et les valeurs dont la valeur est 'chien' ou
# la valeur est 'poisson'
print("\nTous les index et les valeurs dont la valeur est 'chien'\
ou la valeur est 'poisson'")
print(s.loc[(s=='chien') | (s=='poisson')])

# Tous les index et les valeurs dont la valeur est 'chien' ou
# la valeur est 'poisson' sont remplacées par 'autres'
print("\nTous les index et les valeurs dont la valeur est 'chien'\
ou la valeur est 'poisson'")
s.loc[(s=='chien') | (s=='poisson')] = 'autre'
print(s)

# Nouveaux tableaux
s1 = pd.Series([1, 2, 3], index=list('abc'))
print("\nSérie s1")
print(s1)
s2 = pd.Series([5, 6, 7], index=list('acd'))
print("\nSérie s2")
print(s2)

# Addition entre les deux tableaux ci-dessus :
# L'opération ne se fait que pour les index identiques
# Et le résultat est toujours un float64
print("\nAddition des tableaux s1 et s2")
print(s1 + s2)

# Pour toutes les opérations dont les index ne sont
# pas identiques, rajout d'une nouvelle valeur
print("\n Nouvelle valeur à ajouter si les index sont différents")
print(s1.add(s2, fill_value=50))
