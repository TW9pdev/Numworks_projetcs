while True:
    try:
        var = int(input("Entre un nombre: "))
        break
    except ValueError:
        print("")

compteur = 2
liste = []

while compteur is not 9:
    if var % compteur == False:
        liste.append(compteur)
        compteur+=1
    else:
        compteur+=1

print(var, "est divisble par: ")
print(liste)