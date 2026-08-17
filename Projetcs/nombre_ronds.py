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
        print(var / compteur, " rond, divisible par", compteur)
        liste.append(compteur)
        compteur+=1
    else:
        print(var/compteur, " virgule, pas divisible par", compteur)
        compteur+=1

print(var, "est divisble par: ")
print(liste)