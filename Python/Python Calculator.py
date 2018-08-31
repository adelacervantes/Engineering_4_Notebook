#python calculator
# By Adela

a = int (input(" Please enter a number, press enter,  and then enter another number"))
b = int (input(" "))

def doMath(a,b,c):
    if (c == 1):
        return str(round((a+b),2))
    if (c == 2):
        return str(round((a-b),2))
    if (c == 3):
        return str(round((a/b),2))
    if (c == 4):
        return str(round((a*b),2))
    if (c == 5):
        return str(round((a%b),2))
        
print("Sum:\t\t" + doMath(a,b,1))
print("Difference:\t" + doMath(a,b,2))
print("Quotient:\t" + doMath(a,b,3))
print("Product:\t" + doMath(a,b,4))
print("Modulo:\t\t" + doMath(a,b,5))


