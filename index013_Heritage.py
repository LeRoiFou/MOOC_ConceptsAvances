"""
Cours : héritage

Éditeur : Laurent REYNAUD
Date : 22-06-2021
"""

s = "Je fais un MOOC sur Python"

class Phrase:
    
    def __init__(self, ma_phrase):
        self.ma_phrase = ma_phrase
        self.mots = ma_phrase.split()
        
    def nb_lettres(self):
        return len(self.ma_phrase)
    
    def __len__(self):
        return len(self.mots)
    
    def __contains__(self, mot):
        return mot in self.mots
    
    def __str__(self):
        return "\n".join(self.mots)
    

class PhraseSansCasse(Phrase):
    "Classe héritant de la super-classe Phrase"
    
    def __init__(self, ma_phrase):
        "Constructeur surchargé"
        
        # Rappel du constructeur de la classe parente
        Phrase.__init__(self, ma_phrase)
        
        # Surcharge de la méthode
        self.mots_lower = {m.lower() for m in self.mots}
        
    def __contains__(self, mot):
        "Méthode spéciale surchargée"
        
        # Pas de rappel de la méthode de la classe parente mais uniquement
        # une surcharge de la méthode spéciale __contains__()
        return mot.lower() in self.mots_lower

p_no = PhraseSansCasse(s)

print(p_no.mots_lower)
print('Mooc' in p_no)
