"""
Cours : conditions et expressions conditionnelles

Dans ce programme on a recours à des expressions conditionnelles dont la présentation
est plus 'appréciable' que le recours aux conditions classiques ainsi que les
conditions ternaires

Modalité pour saisir ce type d'instruction : 
<résultat_si_vrai> if <condition> else <résultat_si_faux>

Éditeur : Laurent REYNAUD
Date : 07-06-2021
"""

"1er CAS"

my_str = "Ceci est un est"

# Méthode classique
if 'e' in my_str:
    print('ok')
else:
    print('non')

# Conditions ternaires
res1 = ('non', 'ok')['e' in my_str]
print(res1)

# Expressions conditionnelles
res2 = 'ok' if 'e' in my_str else 'non'
print(res2)

"2ème CAS"
print('*' * 50)

my_num = 2.5

# Méthode classique
if my_num < 0:
    print('valeur négative')
elif 0 <= my_num <= 5:
    print('valeur comprise entre 0 et 5')
else:
    print('valeur au-dessus de 5')

# Conditions ternaires
# Compliqué...

# Expressions conditionnelles
res = 'valeur négative' if my_num < 0 else (
    'valeur comprise entre 0 et 5' if 0 <= my_num <= 5 else (
        'valeur au-dessus de 5'))
print(res)

"3ème CAS"
print('*' * 50)

s = 'berlin'

# Méthode classique
if 'a' in s:
    print('avec a')
elif 'b' in s:
    print('avec b')
elif 'e' in s:
    print('avec e')
else:
    print('sans a ni b ni e')

# Expressions conditionnelles
res = 'avec a' if 'a' in s else(
    'avec b' if 'b' in s else(
        'avec e' if 'e' in s else(
            'sans a ni b ni e'
        )
    )
)
print(res)

"4ème CAS"
print('*' * 50)

my_list = list(range(5))
print('liste en entree:', my_list, 'de taille', len(my_list))

# Méthode classique
if  my_list.pop(0) <= 0:
    print('cas 1')
elif  my_list.pop(0) <= 1:
    print('cas 2')
elif my_list.pop(0) <= 2:
    print('cas 3')
else:
    print('cas 4')
print('liste en sortie de taille', len(my_list))

my_list = list(range(5))

# Expressions conditionnelles
res_list = 'cas 1' if my_list.pop(0) <= 0 else(
    'cas 2' if my_list.pop(0) <= 1 else(
        'cas 3' if my_list.pop(0) <= 2 else(
            'cas 4'
        )
    )
)
print(res_list)
print('liste en sortie de taille', len(my_list))

"5ème CAS"
print('*' * 50)

print("Entrez votre âge :")
age = int(input())

# Méthode classique
if age < 18:
    print("mineur")
elif age > 18:
    print("majeur")
else:
    print("18 ans tout pile")

# Expressions conditionnelles
result_age = "mineur" if age < 18 else(
    "majeur" if age > 18 else(
        "18 ans tout pile"
    )
)
print(result_age)

"5ème CAS"
print('*' * 50)

def red():
    print('Rouge')

def green():
    print('Vert')

def blue():
    print('Bleu')

def error():
    print('Erreur de saisie')

color = input('Couleur (RGB) : ')

# Méthode classique
if color == 'rouge':
    red()
elif color == 'vert':
    green()
elif color == 'bleu':
    blue()
else:
    error()

# Expressions conditionnelles
result_color = red() if color == 'rouge' else(
    green() if color == 'vert' else(
        blue() if color == 'bleu' else(
            error()
        )
    )
)
