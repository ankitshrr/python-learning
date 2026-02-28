"""
water -1
snake 0
gun 1
"""

import random

computer = random.choice([0, 1, -1])
YouStr = input("enter the numer")
GameDictionary = {"s": 0, "w": -1, "g": 1}
RverseDict = {0: "water", 1: "gun", -1: "Water"}

You = GameDictionary[YouStr]
print(f"Computer chose {RverseDict[computer]} \n You chose {RverseDict[You]}")

if computer == You:
    print("its draw")
else:
    # if computer == -1 and You == 0: -1
    #     print("you win!")
    # elif computer == -1 and You == 1: -2
    #     print("computer won")
    # elif computer == 0 and You == -1: 1
    #     print("computer won")
    # elif computer == 0 and You == 1:-1
    #     print("you win")
    # elif computer == 1 and You == -1: 2
    #     (" YouStr win")
    # elif computer == 1 and You == 0:1
    #     print("compuuter won")
     if (computer - You) == -1 or  (computer - You) == 2 :
       print("yOU WIN")
     else:
      print("computer win")