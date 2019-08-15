vyska = int(input("Veľkosť: "))

if vyska < 3 or vyska % 2 != 1:
    print("Neviem vytvoriť taký smaragd")

else:
    vyska = (vyska // 2) + 1

    # Horná časť
    for riadok in range(vyska):
        medzery = vyska - riadok - 1
        dute = 2 * riadok - 1

        print(" " * medzery, end="")
        if riadok == 0:
            print("*")
        else:
            print("*" + " " * dute + "*")

    # Dolná časť
    for riadok in range(1, vyska):
        medzery = riadok
        dute = 2 * (vyska - riadok) - 3

        print(" " * medzery, end="")
        if riadok == vyska - 1:
            print("*")
        else:
            print("*" + " " * dute + "*")
