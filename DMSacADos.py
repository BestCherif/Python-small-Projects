
n = int(input("Declarez le nombre d'objet que vous souhaitez a apprendre: "))#declaration de nombre d'objet on veut prendre
MaxP = float(input("Donnez poids maximum que vous pouvez mettre dans le sac(en KG): "))#declaration de maximum de poids qu'on peut mettre dans le sac
Les_objets = []#on declare la matrice qu'on veut lister les objets qu'on veut prendre
sac = []#on declare le sac ou en veut mettre les objets (pas forcement au debut ici)
for j in range(1,n+1):#rotation n fois pour ajouter les n objets dans la list d'objets
    #on veut declarer une list vide au debut de chaque rotation pour qu'on peut ajouter nouveau objet
    List = []
    #la liste est dans la boucle For car nous avons besoin qu'elle soit vide à chaque fois que nous voulons ajouter un nouvel objet
    List.append(str(input("Entrez le nom de votre objet: ")))
    List.append(float(input("Donnez le poids de ce objet(en KG): ")))
    importance = float(input("Évaluer l'importance de l'objet (sur 10): "))
    while importance < 0 or importance > 10:
        importance = float(input("SVP,Évaluer l'importance de l'objet sur 10 pour faciliter les choses: "))
    List.append(importance)
    Les_objets.append(List)


Les_objets.sort(reverse=True, key=lambda objet: objet[2])
#on a tri la matrice "Les_objets" D'apres l'importance de chaque objet en order decroissante
#j'ai trouve la fonction anonymous lambda dans W3school website et sur ChatGPT
#reverse= true , d'apres W3School website, pour le tri en ordre decroissante


for o in range(0,n):# range (0.n) pour utiliser o comme indice
    if Les_objets[o][1] <= MaxP:
        sac.append(Les_objets[o])
        #on peut preciser qu'on ajoute que le nom de l'objet sans son poid et son importance en remplacant Les_objets[o] par Les_objets[o][0]
        MaxP = MaxP-Les_objets[o][1]


print("Les objets qu'on peux mettre dans le sac sont: ", end='')
#end='' pour qu'on peut "print" juste après celle-ci sans sauter une ligne
for object in sac:
    print(object[0], end=', ')
    #la meme chose pour end=', ', pour separer nom des objets avec la vergule et un espace
    #de cette façon, nous évitons d'écrire les parenthèses
