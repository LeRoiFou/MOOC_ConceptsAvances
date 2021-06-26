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

Les dataframe sont des tableaux à 2 dimensions sur lesquels on va mettre
des index sur les lignes et sur les colonnes

Éditeur : Laurent REYNAUD
Date : 25-06-2021
"""

import numpy as np
import pandas as pd

# Une liste de prénoms
prenoms = ['liz', 'bob', 'bill', 'eve']

# Une series d'âge
age = pd.Series([25, 30, 35, 40],
                index=prenoms)

# Une series de taille
taille = pd.Series([160, 175, 170, 180],
                   index=prenoms)

# Une series de liste de sexe
sexe = pd.Series(list('fhhf'),
                 index=prenoms)


"""Constitution d'une dataframe :
-> les entêtes des lignes constituent sont les index
-> les entêtes des colonnes sont les clés de la bibliothèque"""

# Dataframe de la liste et des series ci-avant
print("\nDataFrame (tableau à 2 dimensions)")
df = pd.DataFrame({'age': age,
                   'taille': taille,
                   'sexe': sexe})
print(df)


"Accès aux éléments de la dataframe"

# Accès aux attributs de l'index
print("\nAccès aux attributs index")
print(df.index)

# Accès aux attributs des colonnes
print("\nAccès aux attributs des colonnes")
print(df.columns)

# Accès aux valeurs du tableau numpy
print("\nAccès aux valeurs du tableau numpy")
print(df.values)

# Parcourir les toutes premières lignes de la dataframe
print('\nAccès aux 2 premières lignes')
print(df.head(2))

# Parcourir les toutes dernières lignes de la dataframe
print('\nAccès aux 2 derniers lignes')
print(df.tail(2))

# Exploration rapide des statistiques de la dataframe
print("\nStatistiques de la dataframe")
print(df.describe())


"Indexation dans les dataframe"

# Accès à une ligne
print("\nDonnées concernant 'liz'")
print(df.loc['liz'])

# Accès à une valeur d'une ligne et d'une colonne
print("\nAge de liz")
print(df.loc['liz', 'age'])

# Accès aux éléments d'une colonne
print("\nTaille de toutes les personnes")
print(df.loc[:, 'taille'])

# Accès à tous les éléments de la dataframe selon une condition
print('\nListe des personnes ayant - de 32 ans')
print(df.loc[df.loc[:, 'age']<32])


"Modification de la dataframe"

# Les données de l'index passent en valeurs de la dataframe
print("\nModification de l'index")
df = df.reset_index()
print(df)

# Renommage de la colonne index modifiée ci-avant
print("\nModification du nom de la colonne 'index'")
df = df.rename(columns={'index': 'prenom'})
print(df)

# Une colonne de la dataframe passe en index cette fois-ci
print("\nColonne des âges en index")
df = df.set_index('age')
print(df)


"Simplification des instructions faites ci-avant"

# Réinitialisation de la dataframe
df = pd.DataFrame({'age': age,
                   'taille': taille,
                   'sexe': sexe})

# Même résultat que les instructions faites dans la partie ci-avant
print("\nMême résultat mais avec une seule instruction")
df = (df.reset_index()
      .rename(columns={'index': 'nom'})
      .set_index('age'))
print(df)


"Alignement d'index"

# 1ère Dataframe contenant que des valeurs 1.00
print("\n1ère Dataframe contenant que des valeurs 1.0")
df1 = pd.DataFrame(np.ones((2, 2)),
                   index=list('ab'),
                   columns=list('xy'))
print(df1)

# 2ème Dataframe contenant que des valeurs 1.00
print("\n2ème Dataframe contenant que des valeurs 1.0")
df2 = pd.DataFrame(np.ones((2, 2)),
                   index=list('ac'),
                   columns=list('xz'))
print(df2)

# Somme des 2 dataframe ci-avant
print("\nSomme des 2 dataframe ci-avant")
print(df1 + df2)

# Intervention sur la somme des 2 dataframe ci-avant
print("\nIntervention sur la somme des 2 dataframe ci-avant")
print(df1.add(df2, fill_value=0))

# Nouvelle intervention pour supprimer la valeur 'Nan' définitivement
df = df1.add(df2, fill_value=0)

# 1ère solution remplacement de la valeur 'Nan' par une autre valeur
# print("\nRemplacement de la valeur 'Nan' par -1")
# df = df.fillna(-1)
# print(df)

# 2ème solution : suppression des lignes contenant la valeur 'Nan'
print("\nSuppression des lignes contenant la valeur 'Nan'")
df = df.dropna()
print(df)
