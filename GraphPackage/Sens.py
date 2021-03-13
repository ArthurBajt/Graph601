from enum import Enum

class Sens(Enum):
    """
    Sens est un type énumérer, permetant de representeer un sens de navigation d'un Noeud a l'autre
    """
    AUCUN = 0
    POSITIF = 1
    NEGATIF = 2