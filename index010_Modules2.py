"""
Cours : les modules

x, y, func et MyClass déclarés ci-dessous, sont des variables
du module index010_Modules1.

Si on aurait effectué 'import index010_Modules1', cette fois-ci
index010_Modules1 serait une variable du module.
Et dans ce cas lorsqu'on veut attribuer une variable à
l'attribut x du module index010_Modules1, il faut effectuer l'instruction
suivante : index010_Modules1.x

Éditeur : Laurent REYNAUD
Date : 16-06-2021
"""

from index010_Modules1 import x, y, func, MyClass

print(x)
print(y)
print(func())
MyClass()
