

class Humain2:
    
    """
Principe d'encapsulation:  
Property() peut prendre plusieurs valeurs: getters,setters,deleter,helper
setter: permet de controler de manipuler l'attribut de maniere correct
        cela peut servir lors de la creation de site web avec python pour gerer les controles de saisis
         

"""
    def __init__(self,nom,age):
        print("creation d'une classe")
        self.nom =nom
        self._age = age
        
    def _getage(self):
        if self._age == 1:
            return str(self._age) + " an"
        elif self._age>1:
            return str(self._age) + " ans"
        else:
            print("{} n'a pas d'age valide".format(self.nom))
    
    age = property(_getage)
h1 =Humain2("jack",0)
print("{} a {}".format(h1.nom,h1.age))
       





