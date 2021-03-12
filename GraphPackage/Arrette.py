from .Noeud import *
from .Sens import *

class Arrette(object):
    def __init__(self, n1: Noeud, n2: Noeud, sens: Sens = Sens.AUCUN):
        self._noeud1 = n1
        self._noeud2 = n2
        self._sens = sens



    def __str__(self):
        return ""