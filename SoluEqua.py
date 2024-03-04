#Cherif Mohamed Akram RO L3 Groupe1 202031085873
def menu(): #on definie le menu pour qu'on peut l'appellez quand nous voulons
    print("de quelle degre est votre equation?")
    print("[1] equation de premier degre ,ax+b=0")
    print("[2] equation de deuxieme degre ax^2")
    print("[0] quitter le programme")

menu()
ans=int(input("votre equation est de degre :"))
while ans != 0:
    if ans == 1:
        a = int(input("donnez la valeur de le coefficient a:"))
        b = int(input("donnez la valeur le constant b:"))
        if a == 0:  # si a=0 on aura le constant b=0 et pas de variable
            if b == 0:
                print("donc on aura 0=0 qui est toujours vrai")
            else:
                print(
                    "votre equation n'a pas de solution et absurd")  # b qui est different de zero ne peut pas etre egal a zero
        else:
            print("solution de votre equation est:", -b / a)
    elif ans == 2:
        a = int(input("donnez la valeur de le coefficient a:"))
        while a == 0:  # a ne peux pas etre 0 or l'equation devient une equation de premier degre
            a = int(input("la valeur de a ne peux pas etre zero, donnez une nouvelle valeur pour a:"))
        b = int(input("donnez la valeur de le coefficient b:"))
        c = int(input("donnez la valeur de le constant c:"))
        D = (b ** 2) - 4 * a * c  # calcule de descriminant
        if D < 0:
            print("L'equation n'a pas de solution reelle")
        elif D == 0:
            print("l'equation admet une solution double x=", -b / 2 * a)
        else:
            print("les solution de l'equation est x1=", (-b + D ** (1 / 2)) / 2 * a, "et x2=",(-b - D ** (1 / 2)) / 2 * a)
    else :
        print("option non valide")
    print()
    menu()
    ans = int(input("votre equation est de degre :"))

print("je te remercie pour utiliser mon programme")