def tout():
  while True:
    try:
      choix = int(input("Entre un nombre: "))
      break
    except ValueError:
      print("")
  
      
  while True:
     try:
        percentage = int(input("Combien de % ? "))
        break 
     except ValueError:
       print("")

  if choix*percentage/100*2 % 2 == False:
    print(int(choix*percentage/100))
    
  else:   
     print(percentage, "% de", choix, "est", choix*percentage/100)
  
  var = input("'Continuer' ou 'Exit': ")
  if var == "Continuer":
     tout()
  if var == "Exit":
     exit()
  
  while var != "Continuer" "Exit":
     var = input("'Continuer' ou 'Exit': ")
     if var == "Continuer":
        tout()
     if var == "Exit":
        exit()

tout()

