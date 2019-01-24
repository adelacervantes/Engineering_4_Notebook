#MSP Python Challenge
#By Adela

repeat = True
answer = str(input("Player 1: Please Enter a Word "))
print ("\n" * 50)
blanks = list('_'*len(answer))
print(blanks)
was = 1
bad = True
myArray = [" ---","  \u2510","  O"," /|\ "," / \ "]
#myArray = ["--- "," \u2510", "\n", "O","\n", " /|\ ", "\n", " /\ "]
def printGuy(lines):
       for i in range(0, lines):
              print(myArray[i])
              
def wrong1():
    print(blanks)
    repeat = True
    bad = True
    was = 1
    while repeat:
           guess = str(input("Player 2: Please attempt to guess the word by typing in letters: "))
           #blanks = [(guess if letter == guess else blank) for blank, letter in zip(blanks, answer)]
           print(''.join(blanks))
           printGuy(was)
           if guess not in answer:
                  was += 1
           for letter in answer:
              if letter == guess: 
                     bad = False
              if bad == True:
                     was = was +1
                     
                     #arr = wrong1()
                     #for line in range(0, was):
                     #       print(arr[line])
                     
              if was == 6:
                     print (" better luck next time :/" )
                     repeat = False
                     
              if "_" not in blanks:
                     print ("\nCONGRATULATIONS! You found the word!" )
                     repeat = ("") in input().lower()
                     repeat = False


wrong1()                  

