def all():

  check_premier = 3
  check_2 = 0

  while True:
    try:
      var=int(input("Entre un nombre: "))
      break
    except ValueError:
      print()

  if var % 2 == 1:
    while var != check_premier:
        if var % check_premier == 0:
            break
        else:
            check_premier += 1
            check_2 += 1
        
  if check_2 != 0:
      print("Le nombre est premier")
  else:
    print("Le nombre n'est pas premier")
      
  while True:
    try:
      var=int(input("0 pour continuer, 1 pour quitter: "))
      if var == 0:
        all()
      elif var == 1:
        exit()
    except ValueError:
      print()

all()  