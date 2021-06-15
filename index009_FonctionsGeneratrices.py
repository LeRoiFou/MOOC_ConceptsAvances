"""
Cours : les fonctions génératrices

L'expression génératrice tout comme les compréhensions 
ne peuvent intervenir que pour une seule expression.

Pour intervenir sur plusieurs expressions on a recours
aux fonctions génératrices avec l'instruction yield.

Tout comme les expressions génératrices, les fonctions
génératrices sont uniquement des itérateurs qui évitent
de stocker en mémoire un objet temporaire, car l'objectif de Python
est d'éviter de stocker des objets temporaires en recourant aux
itérateurs.

Éditeur : Laurent REYNAUD
Date : 14-06-2021
"""

"Fonction classique avec un return pour un retour de résultat"
def func():
    return 10

print(func()) # résultat : 10

"""L'appel d'une fonction génératrice créé un objet itérateur"""
def gen():
    yield 10

print(gen()) # résultat : <generator object gen at .....>

"""Recours à la méthode spéciale __next__ pour les itérateurs:
un itérateur va parcourir tous les éléments de l'objet et s'arrête"""
g = gen()
print(next(g)) # résultat : 10
# print(next(g)) # résultat : StopIteration car on est arrivé au bout de l'objet
