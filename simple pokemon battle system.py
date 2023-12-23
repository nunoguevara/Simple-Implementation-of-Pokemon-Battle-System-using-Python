import time as tm
import random as rm
import math
import os

pkm = ["Rattata", "Pidgey"]

x = 20
y = 20

a = [2, 3, 5, 1, 2, 2, 2, 2, 2]
b = [2, 2, 5, 2, 1, 2, 2, 1, 2]

class game:
    def battle():
        y = 20
        x = 20
        print("You find a pokemon")
        chc = str(input("Want to identify the pokemon or run? IP/R: "))
        if chc == "IP":
           while True:
               pkmr = rm.choice(pkm)
               print("The pokemon is: ", pkmr)
               tm.sleep(0.1)
               while True:
                   print("Choose a move to attack it")
                   print("1. Scratch")
                   print("2. -")
                   print("3. -")
                   print("4. -")
                   chc1 = str(input("Input your move: "))
                   if chc1 == "1":
                      ar = rm.choice(a)
                      br = rm.choice(b)
                      print("Charmander! use Scratch!")
                      y -= ar
                      print("You hit the pokemon opponent, HP = ", y, "/20")
                      tm.sleep(0.5)
                      print(pkmr+" use Tackle")
                      x -= br
                      print("Charmander health: ", x, "/20")
                      if y <= 0:
                          print(pkmr+" has fainted")
                          break
                      elif x <= 0:
                          print("Charmander has fainted")
                          break
                  
                   else:
                      print("Invalid choice")
                      tm.sleep(2)
                      os.system('cls' if os.name == "nt" else 'clear')
               break
                  
        elif chc == "R":
              print("Successfuly Run Away...")
              tm.sleep(1)
        else:
           print("The choice doesn't exist(invalid)")

while True:                      
    game.battle()
  
