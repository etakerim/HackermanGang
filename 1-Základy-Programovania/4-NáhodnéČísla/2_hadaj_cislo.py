import random

hadaj = random.randint(1, 100)

while True:
    tip = int(input("Hádaj číslo: "))

    if tip > hadaj:
        print("Veľa")
    elif tip < hadaj:
        print("Málo")
    else:
        print("Uhádol si")
        break
