#Strings and Loops
#By Adela

repeat = True
while repeat:
    words = str(input( "Please type a sentence:"))
    words1 = words.split()
    for word in words1:
        print ("-")
        for letter in word:
            print(letter)
            
