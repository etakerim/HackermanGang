import random

# Vygenerovať náhodné číslo 1..100
hadaj = random.randint(1, 100)

# Pýtam sa na tip
while True:
    tip = int(input("Hádaj: "))

    # Ak sú zhodné tak výhra a koniec
    if tip > hadaj:
        print("Príliš veľa")
    elif tip < hadaj:
        print("Príliš málo")
    else:
        print("JUHÚ")
        break
