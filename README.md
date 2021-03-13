# Graph601
Un package python, utile pour la représentation des graph.


### Modéliser un graph :
Commencer par placer le dossier du package dans votre environement de trvail:

    MonSuperProjet
    ├─MonMain.py
    ├─GraphPackage
    . ├─__init__.py
    . ├─Noeud.py
    . ├─ .
    . ├─ ... ect

Dans votre Main.py:
```python
# Importez les Classes du package
from GraphPackage import *

# Initialisez votre graph
monGraph = Graph()

# Creez quelques Noeud afin de remplir votre Graph
n1 = Noeud("1") # Notez que le nom est facultatif
n2 = Noeud("2")
n3 = Noeud("3")
n4 = Noeud("4")

monGraph.ajouterNoeud(n1)
monGraph.ajouterNoeud(n2)
monGraph.ajouterNoeud(n3)
monGraph.ajouterNoeud(n4)

# Et reliez vos Noeuds
graph.relierNoeuds(n1, n3)
graph.relierNoeuds(n1, n4)
graph.relierNoeuds(n3, n2)

```
