
class Noeud(object):
    def __init__(self, nom: str = ""):
        self._nom=nom
        self._valeur = None
        self._enfants = []

    def getNom(self)->str:
        return self._nom

    def setValeur(self, val):
        self._valeur = val

    def getValeur(self):
        return self._valeur

    def getEnfants(self)->list:
        return self._enfants

    def setEnfants(self, enfants: list):
        self._enfants = enfants

    def ajouteEnfant(self, enfant):
        if (type(enfant) == Noeud) and (not enfant in self._enfants):
            self._enfants.append(enfant)

        else:
            print("Ajout d'enfent impossible !")

    def RetireEnfant(self, enfant):
        self._enfants.remove(enfant)



    def __str__(self):
        res = "("
        if len(self._nom) > 0:
            res += "\"" + self._nom + "\""
        else:
            res += "<Noeud>"

        if self._valeur != None:
            res += f"\tvaleur : {self._valeur} "
        res += ")"

        return res