import random

while True:
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    print(f"\nKoľko je {x} x {y}?")
    vysledok = int(input("= "))

    while vysledok != x * y:
        print("Nesprávne - hádaj znovu")
        vysledok = int(input("= "))

    print("Správne - len tak ďalej")

    pokracuj = input("Chceš ďaľší príklad? (a / n): ")
    if pokracuj == 'n':
        break
