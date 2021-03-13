from GraphPackage import *
from Res import graph

print(graph)
parcourLargeur = graph.parcourLargeur( graph.getNoeuds()[3] )
parcourProfondeur = graph.parcourProfondeur( graph.getNoeuds()[3] )

for i in parcourLargeur:
    print(i)

for j in parcourProfondeur:
    print(j)

