def tout():
  while True:
    try:
      choix = int(input("Entre un nombre"))
      break
    except ValueError:
      print("")
  
      
  while True:
     try:
        percentage = int(input("Combien de % ?"))
        break 
     except ValueError:
       print("")

  if choix*percentage/100 % 2 == False:
    print(int(choix*percentage/100))
    
  else:   
     print(percentage, "% de", choix, "est", choix*percentage/100)
  
  while True:
      try:
         var = int(input(" '0' pour continuer, '1 pour quitter"))
         break
      except ValueError:
         print()
   
  if var == 0:
     tout()
  if var == 1:
    exit()

tout()