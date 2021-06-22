"""Cours : Classes & instances

Éditeur : Laurent REYNAUD
Date : 16-06-2021"""

class Car:
    
    roue = 4 # attribut de classe
    
    def __init__(self, marque='Fiat'):
        
        self.marque = marque # attribut d'instance
        Car.roue += 1
        
car1 = Car()
print(car1.marque)
print(car1.roue)
car2 = Car("Renault")
print(car2.marque)
print(car2.roue)