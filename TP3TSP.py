#Cherif Mohamed Akram RO L3 Groupe1 202031085873

import math
def Distance(pointx,pointy):
    X = pointx
    Y = pointy
    distance = math.sqrt((X ** 2) + (Y ** 2))#car on change point d'origin, on n'a pas besoin de fair math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance

n = int(input("Declarez le nombre de ville que vous voulez parcourir: "))#declaration de nombre d'objet on veut prendre

Les_Villes = []#on declare la matrice qu'on veut lister les villes qu'on veut parcourir
Order_Ville = []#on declare la List ou en veut mettre les villes en ordre (pas forcement au debut ici)

for j in range(1,n+1):#rotation n fois pour ajouter les n ville dans la list des villes
    #on veut declarer une list vide au debut de chaque rotation pour qu'on peut ajouter nouvelle ville
    List = []
    Ville = str(input("Entrez le nom de ville: "))
    List.append(Ville)
    x = float(input(f"Donnez le coordonne x pour {Ville}: "))
    List.append(x)
    y = float(input(f"Donnez le coordonne y pour {Ville}: "))
    List.append(y)
    List.append(Distance(x,y))
    Les_Villes.append(List)


CalcDis = sorted(Les_Villes,reverse=True, key=lambda Dis: Dis[3])

for i in range(n):
    Order_Ville.append(CalcDis[len(CalcDis)-1])
    #print(Order_Ville)
    del CalcDis[len(CalcDis)-1]#on supprime la ville qu'on a parcouru pour ne pas la parcourir une autre fois

    for j in range(n-i-1):#changement de coordonne apres changement de point origine
        CalcDis[j][1] = CalcDis[j][1] - Order_Ville[i][1]
        CalcDis[j][2] = CalcDis[j][2] - Order_Ville[i][2]
        CalcDis[j][3] = Distance(CalcDis[j][1],CalcDis[j][2])
        #print(CalcDis)
    CalcDis.sort(reverse= True, key=lambda Dis: Dis[3])#sort pour l'ordonne une autre fois d'apres la nouvel distance de chaque ville a le nouvel point d'origin
    # print(CalcDis)


print("L'order de Villes a Parcourir pour la plus court distance est: ", end='')
for ville in Order_Ville:
    print(ville[0], end=', ')