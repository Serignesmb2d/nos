#creation de la classe 

class Humain:
    hc = 0
    def __init__(self,cprenom,cage=1):
       print("creation d'un humain")
       self.prenom = cprenom
       self.age = cage 
       Humain.hc += 1

h1 =Humain("jojo")
print("le prenom saisi est" ,h1.prenom, "son age est de ",h1.age)
print("humain cree est de numero {}".format(Humain.hc))


h2 =Humain("faye")
print("le prenom saisi est" ,h2.prenom, "son age est de ",h2.age)
print("humain cree est de numero {}".format(Humain.hc))
#En python les accesseurs sont pas trop demander c aa d on peut s'en passer
 



