import math


nb_sommets = int(input("Entrez le nombre de sommets : "))# Obtenir le nombre de sommets de l'utilisateur


sommets = ['s'] + [str(i) for i in range(1, nb_sommets)]# on declare la liste des sommets avec on note chaque sommets par leur indice sauf le sommets 's'


arcs = []# on declare la matrice des arcs
for _ in range(int(input("Entrez le nombre d'arcs : "))):
    debut, fin, longueur = input("Entrez l'arc (début, fin, longueur) : ").split()
    arcs.append([debut, fin, float(longueur)])

# on declare la matrice des potential des sommets qui on va utiliser pour les iterations de l'algorithm
potentiels = {sommet: math.inf for sommet in sommets}
potentiels['s'] = 0  # on a le premier sommet , sommet de depart, 's'

S = set()  # ensemble de sommets qu'on a trouver leur potentiel

while len(S) < nb_sommets:
    #
    sommet_min = min((s for s in sommets if s not in S), key=lambda x: potentiels[x])
    S.add(sommet_min)

    # on trouve les potentiels des sommets adjacent a sommet_min
    for arc in arcs:
        if arc[0] == sommet_min:
            sommet_dest = arc[1]
            longueur = arc[2]
            if potentiels[sommet_min] + longueur < potentiels[sommet_dest]:
                potentiels[sommet_dest] = potentiels[sommet_min] + longueur

print("Chemins les plus courts :") #affichage des sommets avec leur potentiel.
for sommet, potentiel in potentiels.items():
    print(f"Sommet : {sommet}, Potentiel : {potentiel}")