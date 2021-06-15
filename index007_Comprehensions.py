"""
Cours : Les compréhensions

Les compréhensions portent aussi bien sur les listes, 
que sur les ensembles et les dictionnaires : 
elles portent donc sur les objets itérables mutables.

Ces compréhensions permettent d'effectuer des traitements sur
des objets itérables.

Les compréhensions vont stocker un objet temporaire,
et qui vont donc prendre de la mémoire à l'inverse d'une
expression génératrice qui économise énormément de mémoire car
celle-ci est uniquement un itérateur et n'est pas itérable 
contrairement à une compréhension

Éditeur : Laurent REYNAUD
Date : 14-06-2021
"""

# compréhension de listes
prenoms = ['ana', 'eve', 'alice', 'ANNE', 'Bob']

a_prenoms = [p.lower() for p in prenoms if p.lower().startswith('a')]
print(a_prenoms)

prenoms.extend(prenoms)
a_prenoms = [p.lower() for p in prenoms if p.lower().startswith('a')]
print(a_prenoms)

# compréhension d'un ensemble qui permet d'éviter les doublons
a_prenoms = {p.lower() for p in prenoms if p.lower().startswith('a')}
print(a_prenoms)

# compréhension de dictionnaire
ages = [('ana', 20), ('EVE', 30), ('bob', 40)]

ages = dict(ages)

ages_fix = {p.lower(): a for p, a in ages.items() if a < 40}
print(ages_fix)
