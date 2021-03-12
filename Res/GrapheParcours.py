from GraphPackage import *

# le Graph
graph = Graph()

# Les Noeuds
n1 = Noeud("1")
n2 = Noeud("2")
n3 = Noeud("3")
n4 = Noeud("4")
n5 = Noeud("5")
n6 = Noeud("6")
n7 = Noeud("7")

# On ajoute les noeuds dans le graphe
graph.ajouterNoeud(n1)
graph.ajouterNoeud(n2)
graph.ajouterNoeud(n3)
graph.ajouterNoeud(n4)
graph.ajouterNoeud(n5)
graph.ajouterNoeud(n6)
graph.ajouterNoeud(n7)

# Les liens
# On relie les noeuds entre eux
graph.relierNoeuds(n4, n7)
graph.relierNoeuds(n4, n1)
graph.relierNoeuds(n1, n7)

graph.relierNoeuds(n1, n3)
graph.relierNoeuds(n3, n2)

graph.relierNoeuds(n7, n5)
graph.relierNoeuds(n7, n6)