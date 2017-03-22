vstup = input("Zadaj: ")
abeceda = []

for i in range(26):
    abeceda.append(0)

# Prejsť reťazcom
for i in range(len(vstup)):
    if vstup[i].isalpha():
        index = ord(vstup[i].upper()) - ord("A")
        abeceda[index] += 1

for i in range(len(abeceda)):
    print(chr(i + ord("A")), end=" ")
    for j in range(abeceda[i]):
        print("*", end="")
    print()
    

"""
for i in range(len(abeceda)):
    print("{} => {}".format(chr(i + ord("A")), abeceda[i]))
""" 
        
        
