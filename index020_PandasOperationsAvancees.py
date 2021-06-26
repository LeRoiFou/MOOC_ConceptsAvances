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

Éditeur : Laurent REYNAUD
Date : 25-06-2021
"""

import pandas as pd
import numpy as np
import seaborn as sns # module des données le titanic :D


"Concaténation entre plusieurs dataframe"

# 1er dataframe
print("\n1er dataframe")
df1 = pd.DataFrame(np.random.randint(1, 10, size=(2, 2)),
                   columns=list('ab'),
                   index=list('xy'))
print(df1)

# 2ème dataframe
print("\n2ème dataframe")
df2 = pd.DataFrame(np.random.randint(1, 10, size=(2, 2)),
                   columns=list('ab'),
                   index=list('zt'))
print(df2)

# Concaténation des 2 dataframe ci-avant en 2 colonnes
print("\nConcaténation des 2 dataframe ci-avant en 2 colonnes")
print(pd.concat([df1, df2]))


# 3ème dataframe
print("\n3ème dataframe")
df3 = pd.DataFrame(np.random.randint(1, 10, size=(2, 2)),
                   columns=list('cd'),
                   index=list('xy'))
print(df2)

# Concaténation du 1er dataframe et du 3ème en 2 lignes
print("\nConcaténation du 1er dataframe et du 3ème en 2 lignes")
print(pd.concat([df1, df3], axis=1))


"Jointure entre plusieurs dataframe"

# Autres dataframe : personnel d'une société -> service & ancienneté
print("\nDataframe personnel affecté au service qui lui est rattaché")
df4 = pd.DataFrame({'personnel': ['Bob', 'Lisa', 'Sue'],
                    'groupe': ['SAV', 'R&D', 'RH']})
print(df4)

print("\nDataframe ancienneté du personnel")
df5 = pd.DataFrame({'personnel': ['Lisa','Bob', 'Sue'],
                    'date embauche': [2004, 2008, 2014]})
print(df5)

# Jointure des deux dataframe ci-avant
print("\nJointure entre les deux dataframe")
print(pd.merge(df4, df5))


"Opérations de regroupement et de pivot"

# Téléchargement des données du Titanic :D
print("\nRecours au module seaborn")
ti = sns.load_dataset('titanic').loc[:, ['survived', 'sex', 'class']]
print(ti.head())

# Affichage du nombre de lignes et de colonnes au total
print("\nNombre total de lignes et de colonnes")
print(ti.shape)

# Accès aux données de la colonne 'survived'
print("\nAccès aux données de la colonne 'survived'")
print(ti.loc[:, 'survived'])

# Taux de survie des personnes du Titanic :D
print("\nTaux de survie des personnes du Titanic")
print(ti.loc[:, 'survived'].mean())

# Différence du taux de survie entre les différentes classes
print("\nTaux de survie des passagers de la 1ère classe")
print(ti.loc[ti.loc[:, 'class']=='First', 'survived'].mean())
print("\nTaux de survie des passagers de la 2ème classe")
print(ti.loc[ti.loc[:, 'class']=='Second', 'survived'].mean())
print("\nTaux de survie des passagers de la 3ème classe")
print(ti.loc[ti.loc[:, 'class']=='Third', 'survived'].mean())

# Récapitulatif du taux de survie par class
print("\nRécapitulatif du taux de survie des passagers par classe")
print(ti.groupby('class').mean())

# Récapitulatif du taux de survie par regroupement classe et sexe
print("\nRécapitulatif du taux de survie par regroupement classe et sexe")
g = ti.groupby(['class', 'sex']).mean()
print(g)

# Recours à la fonction pivot_table
print("\nNouvelle représentation avec la fonction pivot_table")
print(ti.pivot_table('survived',
                     aggfunc=np.mean,
                     index='class',
                     columns='sex'))
