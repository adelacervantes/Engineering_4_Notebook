# Automatic dice roller
# by Adela


print ("AutoMatic dice Roller")
from random import randint
repeat = True
while repeat == True:

    print ("roll "+ str(randint(1,6)))

    if ("x") in input():
        repeat = False
