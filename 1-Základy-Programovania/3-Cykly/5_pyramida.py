vyska = int(input("Výška pyramídy: "))
print()

for riadok in range(vyska):
    medzery = vyska - riadok - 1
    dute = 2 * riadok - 1

    print(" " * medzery, end="")
    if riadok == 0:
        print("*")
    elif riadok == vyska - 1:
        print("*" * (dute + 2))
    else:
        print("*" + " " * dute + "*")
