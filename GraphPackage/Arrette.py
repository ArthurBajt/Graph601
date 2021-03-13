from .Noeud import *
from .Sens import *

class Arrette(object):
    """
    Une Arrette est la relation qui relie 2 Noeuds entre eux
    """
    def __init__(self, n1: Noeud, n2: Noeud, sens: Sens = Sens.AUCUN):
        self._noeud1 = n1
        self._noeud2 = n2
        self._sens = sens

    # getters & Setters ---
    def getNoeud1(self)->Noeud:
        return self._noeud1

    def setNoeud1(self, nd: Noeud):
        self._noeud1 = nd

    def getNoeud2(self) -> Noeud:
        return self._noeud2

    def setNoeud2(self, nd: Noeud):
        self._noeud2 = nd

    def getSens(self)->Sens:
        return self._sens

    def setSens(self, sens: Sens):
        self._sens = sens

    # Methodes de Python
    def __str__(self):
        s = "--"

        if self._sens == Sens.POSITIF:
            s = "-->"

        elif self._sens == Sens.NEGATIF:
            s = "<--"

        return f"( {self._noeud1.__str__()}\t{s}\t{self._noeud2.__str__()})"