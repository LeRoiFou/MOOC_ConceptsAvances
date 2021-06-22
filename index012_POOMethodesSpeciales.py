"""
Cours : méthodes spéciales dans les classes

Les méthodes spéciales dans les classes permettent de se comporter
comme ci lorsqu'on instancie la classe, on appliquerait une méthode
spéciale du module par défaut built-in.
Sans définir ces méthodes spéciales dans les classes, si on appelle 
directement les méthodes spéciales du module par défaut built-in
lorsqu'on instancie les classes, ces méthodes ne fonctionnent pas.

Liste des méthodes spéciales :
https://docs.python.org/3/reference/datamodel.html#specialnames

Éditeur : Laurent REYNAUD
Date : 17-06-2021
"""

class Phrase:
    
    def __init__(self, ma_phrase):
        "Et oui... méthode spéciale pour le constructeur"
        self.ma_phrase = ma_phrase
        self.mots = ma_phrase.split()
    
    def nb_lettres(self):
        "Méthode sur le nombre de caractères dans la phrase"
        
        return len(self.ma_phrase)
    
    def __len__(self):
        """"Méthode spéciale sur le nombre de mots dans
        la phrase :
        Sans définir cette méthode spéciale dans la classe, 
        lorsqu'on appelle directement cette méthode, il y
        aura un message d'erreur.
        Cette méthode se comporte comme une méthode spéciale
        du module par défaut built-in qui marche par exemple
        pour une str"""
        
        return len(self.mots)
    
    def __contains__(self, mot):
        """Méthode spéciale pour savoir si le mot recherché
        est dans la phrase
        Sans définir cette méthode spéciale dans la classe, 
        lorsqu'on appelle directement cette méthode, il y
        aura un message d'erreur indiquant que la classe
        n'est pas itérable.
        Cette méthode se comporte comme une méthode spéciale
        du module par défaut built-in qui marche par exemple
        pour une str"""
        
        return mot in self.mots
    
    def __str__(self):
        """Méthode spéciale pour afficher le résultat souhaité"""
        
        return "\n".join(self.mots)

# instanciation de l'objet classe Phrase
p = Phrase("Je fais un mooc sur Python")

# appel de la méthode spéciale __len__()
print(len(p))

# recours de la méthode spéciale __contains__()
print('test' in p)

# recours de la méthode spéciale __str__()
print(p)