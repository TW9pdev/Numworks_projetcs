from math import *

def all():

  while True:
    try:
      var=int(input("Entre un nombre: "))
      break
    except ValueError:
      print()
      
  if fmod(var, 2) == True:
    print(var, "est premier.")
  else:
    print(var, "n est pas premier.")
    
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