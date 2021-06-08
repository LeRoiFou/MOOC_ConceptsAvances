"""
Cours : conditions et expressions conditionnelles

Dans ce programme on a recours à la boucle while
Avec cette boucle il faut toujours penser qu'on peut recourir :
-> aux instructions continue et break
-> à une boucle infinie avec while True

Éditeur : Laurent REYNAUD
Date : 07-06-2021
"""

print("\nWhile et l'instruction continue\n")
"""Avec l'instruction continue on 'saute' la ligne pour laquelle
l'instruction continue va s'appliquer"""

a = list(range(1, 11))
print(a)

while a:
    a.pop(0)
    if len(a) == 5 :
        continue # la ligne avec 5 composants ne sera pas affichée
    print(a)

print("\nWhile et l'instruction break\n")
"Avec l'instruction break on 'casse la boucle'"

a = list(range(1, 11))
print(a)

while a:
    a.pop(0)
    if len(a) == 5 :
        break # on sort de la boucle dès qu'il reste 5 composants
    print(a)

print("\nBoucle infinie avec while True\n")

while True: # boucle infinie
    "Tant que la réponse n'est pas 'aucune', une question s'affiche"
    s = input("Quelle est votre question ?\n")
    if "aucune" in s:
        break