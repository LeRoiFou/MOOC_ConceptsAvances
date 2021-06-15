"""
Cours : itérables et itérateurs

Un itérable est une str, liste, tuple, ensemble, dictionnaire, fichier...
c'est à dire qu'on peut parcourir l'objet concerné notamment avec
la boucle for.
Un itérable est donc un objet qui peut-être bouclé.
Donc un boléen, un int, un float... sont des objets non itérables
La méthode spéciale __iter__ présente dans un objet indique que
celui-ci est itérable (voir les exemples ci-dessous)

Les objets itérables ne sont pas des itérateurs : en effet,
la méthode spéciale __next__ n'est pas présente dans l'objet
concerné.
Cependant lorsqu'on appelle la méthode spéciale __iter__, celle-ci
retourne un nouvel objet qui est un itérateur.
Un itérateur ne parcourt qu'une seule fois tous les éléments de
l'objet itérable et lorsqu'il n'y a plus d'éléments à parcourir,
il y a l'instruction "StopIteration" qui s'applique.

Un itérateur dispose :
-> de la méthode spéciale __iter__
-> de la méthode spéciale __next__
-> de l'instruction StopIteration
Un itérateur est un objet itérable : un itérateur parcourt les 
éléments d'un objet qui est itérable.

Un objet n'est pas forcément itérable et itérateur. 
À titre d'exemple un fichier n'est pas un itérable mais c'est
un itérateur qui va parcourir ligne par ligne les fichiers contenus
mais le fait que ce ne soit pas un itérateur, l'objet ne sera pas
mis en mémoire ce qui aura de l'importance au regard de la taille
du fichier

Éditeur : Laurent REYNAUD
Date : 14-06-2021
"""

"""Pour savoir si un objet est itérable, il suffit de recourir
 à la fonction native dir() et de voir si l'objet en question
 dispose de la méthode spéciale __iter__"""

# La méthode spéciale __iter__ est présente pour les objets suivants :
print("\nSéquences : les chaînes de caractères")
print(dir(str))
print("\n\nSéquences : les listes")
print(dir(list))
print("\n\nSéquences : les tuples")
print(dir(tuple))
print("\n\nLes ensembles")
print(dir(set))
print("\n\nLes dictionnaires")
print(dir(dict))

# La méthode spéciale __iter__ n'est pas présente pour les objets suivants :
print("\nLes booléens")
print(dir(bool))
print("\nLes entiers")
print(dir(int))
print("\nLes réels")
print(dir(float))
print("\nLes fonctions")
def func(a):
    return a
print(dir(func))

"""En exécutant la méthode spéciale __iter__ sur un objet itérable,
elle renverra un itérateur car cette fois-ci, la méthode spéciale
__next__ est présente et qui confirmera que c'est un itérateur"""
print("\n\n\nLes itérateurs")
my_list=[2]
my_list_iterator = iter(my_list)
print(dir(my_list_iterator))
