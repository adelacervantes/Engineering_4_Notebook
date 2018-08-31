#Quadratic Equation Calculator
#by Adela

import math
print("Quadratic Solver")
a = float(input("please enter a coefficient for a"))
b = float(input("please enter a coefficient for b "))
c = float(input("please enter a coefficient for c "))
disc = float
x = float
x1 = float
disc = (b**2 - 4*a*c)
#x = (-b + math.sqrt(b**2 - 4*a*c))/2*a
#x1 = (-b - math.sqrt(b**2 - 4*a*c))/2*a
def doQuads(a,b,c):
#   d = true
    if (disc < 0):
        print (" No Solution")
    if (disc == 0 ):
        x = (-b + math.sqrt(b**2 - 4*a*c))/2*a
        myArray = [x]
        return myArray
    if (disc > 0):
        x = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
        x1 = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)
        myArray = [x, x1]
        return myArray
print (doQuads(a,b,c))
    #print(disc, x, x1)
if (disc > 0):
    print(" ")
if (disc == 0):
    print("  ")
if (disc < 0):
    print("  ")
    
