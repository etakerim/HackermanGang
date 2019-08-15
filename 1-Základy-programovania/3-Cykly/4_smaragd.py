vyska = int(input("Veľkosť: "))

if vyska < 3 or vyska % 2 != 1:
    print("Neviem vytvoriť taký smaragd")

else:
    vyska = (vyska // 2) + 1

    # Horná časť
    for riadok in range(vyska):
        medzery = vyska - riadok - 1
        hviezdy = 2 * riadok + 1
        print(" " * medzery + "*" * hviezdy)

    # Dolná časť
    for riadok in range(1, vyska):
        medzery = riadok
        hviezdy = 2 * (vyska - riadok) - 1
        print(" " * medzery + "*" * hviezdy)
