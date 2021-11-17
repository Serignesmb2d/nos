"""
Methode : fonction sur une instance
Methode statique : fonction  sur une classe
Methode statique : fonction independante mais "lié" a une classe

"""
class Humain1 : 

    lieuhabitation = "Mars"
    
    def __init__(self,prenom,nom):
        self.prenom = prenom
        self.nom = nom

    def manger(self,bouffe):
        print("{} a manger du {}".format(self.prenom,bouffe))
        
    def changer_planete(cls, np):
        Humain1.lieuhabitation = np
        
    changer_planete = classmethod(changer_planete)
    
    def definition():
        print("salut")
        
    definition =staticmethod(definition)
        
   
#remarque cls renvoi variable de classe et self variable standard

h1 = Humain1("awa","dia")
h1.manger("yassa poulet")
print("Planet actuelle est {}".format(Humain1.lieuhabitation))
Humain1.changer_planete("Terre")
print("Planet en cours est {}".format(Humain1.lieuhabitation))
Humain1.definition()