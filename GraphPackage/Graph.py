from .Arrette import *
from .Noeud import *
from .Sens import *


class Graph(object):
    def __init__(self):
        self._noeuds = []
        self._arrettes = []
        pass

# -------------------------------------
    def parcourLargeur(self, nd: Noeud)-> list:
        assert (nd in self._noeuds), "Le Noeud n'est pas dans le graphe !"
        res = []
        file = [nd]
        marque = []  # Les noeuds deja vu ou "marquées"

        while (len(file) != 0):
            nd = file[0]
            file.remove(file[0])
            marque.append(nd)
            res.append(nd)

            for enf in nd.getEnfants():
                if not enf in marque:
                    file.append(enf)
                    marque.append(enf)

        return res

    def parcourProfondeur(self, nd: Noeud, marque=[]) -> list:
        res = [nd]
        marque.append(nd)

        for enf in nd.getEnfants():
            if not enf in marque:
                res += self.parcourProfondeur(enf, marque)

        return res

# -------------------------------------
    def ajouterNoeud(self, nd: Noeud):
        if not nd in self._noeuds:
            self._noeuds.append(nd)

        else:
            print("le noeud existe deja !")

    def SuprimeNoeud(self ,nd: Noeud):
        self._noeuds.remove(nd)

    def relierNoeuds(self, n1: Noeud, n2: Noeud, sens: Sens= Sens.AUCUN):
        if (n1 in self._noeuds) and (n2 in self._noeuds):
            arrette = Arrette(n1, n2, sens)
            self._arrettes.append(arrette)

            if sens == Sens.POSITIF:
                n1.ajouteEnfant(n2)

            elif sens == Sens.NEGATIF:
                n2.ajouteEnfant(n1)

            else:   # Sens.AUCUN
                n1.ajouteEnfant(n2)
                n2.ajouteEnfant(n1)


        else:
            print("Tout les noeuds ne sont pas dans le graph")

# -------------------------------------

    def setNoeuds(self, tab: list):
        self._noeuds = tab

    def getNoeuds(self) -> list:
        return self._noeuds


    def setArrettes(self, tab: list):
        self._arrettes = tab

    def getArrettes(self) -> list:
        return self._arrettes



    def __str__(self):
        res = f"Graph de {len(self._noeuds)} noeud(s), et {len(self._arrettes)} arrette(s)\n"
        for nd in self._noeuds:
            res += "\t- " + nd.__str__() +"\n"
        return res