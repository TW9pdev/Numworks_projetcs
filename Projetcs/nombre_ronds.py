def tout():   
    while True:
        try:
            var = int(input("Entre un nombre: "))
            break
        except ValueError:
            print("")

    compteur = 2
    liste = []

    while compteur is not 26:
        if var % compteur == False:
            liste.append(compteur)
            compteur+=1
        else:
            compteur+=1

    if not liste:
        print(var, "n'est pas divisible")
    else:
        print(var, "est divisble par: ")
        print(liste)

    choix = input("'Continuer' pour continuer, 'Exit' pour quitter")
    if choix == "Continuer":
        tout()
    elif choix == "Exit":
        exit()
    else:
        while choix not in "Continuer" "Exit":
            try:
                choix = input("'Continuer' pour continuer, 'Exit' pour quitter")
                if choix == "Continuer":
                    tout()
                elif choix == "Exit":
                    exit()
            except ValueError:
                print("")

tout()