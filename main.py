#1
print("#1")
class Domino:
  def __init__(self, faceA, faceB):
    self.faceA = faceA
    self.faceB = faceB

  def affiche_points(self):
    print("face A : " + str(self.faceA) + " face B : "  + str(self.faceB))
  
  def valeur(self):
    return (self.faceA + self.faceB)

d1 = Domino(2, 6)
d2 = Domino(4, 3)

d1.affiche_points()
d2.affiche_points()

print("Total des points :", d1.valeur() + d2.valeur())
print(" ")

#2
print("#2")
class CompteBancaire:
  def __init__(self, nom="Dupont", solde=1000):
    self.nom = nom
    self.solde = solde

  def depot(self, somme):
    self.solde = self.solde + somme

  def retrait(self, somme):
    self.solde = self.solde - somme

  def affiche(self):
    print("Le solde du compte bancaire de", self.nom, "est de :", self.solde)


compte1 = CompteBancaire('Duchmol', 800)
compte1.depot(350)
compte1.retrait(200)
compte1.affiche()

compte2 = CompteBancaire()
compte2.depot(25)
compte2.affiche()

print(" ")


#3
print("#3")

class Voiture:

  pilote = "void"
  vitesse = 0
  
  def __init__(self, marque = 'Ford', couleur = 'rouge'):
    self.marque = marque
    self.couleur = couleur

  def choix_conducteur(self, nom):
    self.pilote = nom

  def accelerer(self, taux, duree):
    if self.pilote=="void":
      print("Cette voiture n'a pas de conducteur !")
    else:
      self.vitesse += taux * duree
      if self.vitesse < 0:
        self.vitesse = 0
  
  def affiche_tout(self):
    print("La {} {} est piloté par {} et a pour vitesse {} km/h".format(self.marque, self.couleur, self.pilote, self.vitesse))

a1 = Voiture('Peugeot', 'bleue')
a2 = Voiture(couleur = 'verte')
a3 = Voiture('Mercedes')

a1.choix_conducteur('Roméo')
a2.choix_conducteur('Juliette')

a1.accelerer(1.8, 12)
a2.accelerer(1.8, 12)
a3.accelerer(1.9, 11)

a2.affiche_tout()
a3.affiche_tout()