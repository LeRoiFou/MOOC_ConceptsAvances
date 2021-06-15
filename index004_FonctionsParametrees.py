"""
Cours : fonctions paramétrées

Dans ce cours on voit la distinction entre une fonction argumentée par défaut
et une fonction argumentée avec des variables définies

Éditeur : Laurent REYNAUD
Date : 07-06-2021
"""

"""Lorsqu'on paramètre une fonction, si celle-ci dispose de + d'un argument,
il est difficile de savoir l'ordre des arguments"""

def func(last_name, first_name, age):
    return {"Nom": last_name, "Prénom": first_name, "Age": age}

print(func("Gerald", 42, "John"))

"""Autre solution pour savoir ce qui est argumenté à quel paramètre 
c'est rattaché"""

def func(last_name, first_name, age):
    return {"Nom": last_name, "Prénom": first_name, "Age": age}

print(func(age=42, first_name="John", last_name="Gerald" ))

"""Cette fois-ci on ne veut pas donner son âge"""

# avec des arguments non nommés
print(func("Gerald", "John", age='?'))

# avec des arguments nommés
print(func(age='?', first_name="John", last_name="Gerald" ))