"""
Cours : les expressions génératrices

L'expression génératrice est un itérateur, qui permet 
contrairement à une compréhension, de ne pas stocker
un objet temporaire, car l'expression génératrice
n'est pas itérable, ce qui permet d'économiser beaucoup
de mémoire.

Autre cas pour lequel l'objet est un itérateur et non
itérable : les fichiers
On ne va pas stocker un fichier temporaire (objet itérable)
pour un fichier de plusieurs Go de mémoire qui va se
cumuler dans la machine...

Sur Python tout est objet et si besoin éviter de générer
des objets temporaires si on veut obtenir au final qu'un
résultat de traitement(s), d'où l'intérêt de recourir aux
expressions génératrices qui économisent énormément de mémoire.

Éditeur : Laurent REYNAUD
Date : 14-06-2021
"""

"Compréhension de liste"
carre = [x**2 for x in range(1000) ]
"""Si on imprime la liste, ça va afficher tous les élements
de la liste temporaire du composant 0 au composant 999"""
print(sum(carre))
print(sum(carre))


"""Expression génératrice :
Différence par rapport à une comprehension de liste : au lieu
de mettre des '[]' on met des '()'"""
carre = (x**2 for x in range(1000))

"""Une expression génératrice n'étant pas itérable, il n'y a
donc pas ici d'objet temporaire, donc quand on veut imprimer
ce que contient l'expression génératrice, celle-ci va générer
juste une référence de l'objet"""
print(carre)

"""Dans cet exemple on veut juste effectuer un traitement
sur un objet itérable, donc pour économiser de la mémoire,
il suffit de recourir à une expression génératrice"""
print(sum(carre))

"""Etant donné qu'une expression génératrice est un itérateur
et par conséquent il parcourt la liste qu'une seule fois, donc
relancer un autre traitement sur l'expression génératrice ne
retournera rien à l'inverse d'une compréhension qui a conservé
en mémoire un itérable temporaire"""
print(sum(carre))