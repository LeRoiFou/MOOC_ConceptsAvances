"""
Cours : portée des variables

Il existe différentes types de variables :
-> Locale : variable locales comprises dans une fonction
-> Englobante : variable englobante qui se trouve dans une fonction
qui comprend une autre fonction dans laquelle il y a des variables locales
-> Globale : variable globale qui est déclarée dans le module (fichier)
-> Built-in : variable built-in qui est dans le module par défaut d'un fichier
python à savoir le module built-in qui dispose de fonction natives qui
sont des objets (print, input...) et donc des variables de type built-in

Les variables globales sont à éviter car les modifications sont implicites et
sont une source de confusion pour les programmes (voir cas ci-dessous)

Exemple également d'une variable englobante qui devient une variable locale

Éditeur : Laurent REYNAUD
Date : 07-06-2021
"""

print("\nOn déclare une variable globale dans une fonction\n")

a = 10

def func():
    global a
    a = a + 10
    print(a)

print(a) # donne 10 pour résultat : ok
func() # donne 20 pour résultat : ok
print(a) # donne 20 pour résultat : aïe -> modification implicite...

print("\nRésolution du problème par des modifications explicites\n")

note = 10

def add_10(n):
    return n + 10

print(note) # donne 10 pour résultat : ok
print(add_10(note)) # donne 20 pour résultat : ok
print(note) # donne 10 pour résultat : ok -> modification explicite

print("\nDistinction des types de variables\n")

a = "variable globale"

def func_1():
    a = "variable englobante"

    def func_2():
        a = "variable locale"
        print(f"La variable 'a' est une variable {a}")

    func_2()
    print(f"La variable 'a' est une variable {a}")

func_1()
print(f"La variable 'a' est une {a}")

print("\nVariable englobante devenue variable locale\n")

a = "variable globale"

def func_1():
    a = "variable englobante"

    def func_2():
        nonlocal a # la variable englobante est devenue une variable locale
        a = "variable locale"
        print(f"La variable 'a' est une variable {a}")

    func_2()
    print(f"La variable 'a' est une variable {a}")

func_1()
print(f"La variable 'a' est une {a}")