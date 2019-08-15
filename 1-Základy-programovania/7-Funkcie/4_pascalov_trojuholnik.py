def pascalov_trojuholnik(n):
    row = [1, 1]
    medzery = n
    pocet = 0

    for i in range(n):
        pocet += 1
        medzery -= 1

        print(" " * medzery, end="")
        for cislo in row[:pocet]:
            print(cislo, end=" ")
        print()

        for j in range(pocet - 1,  0, -1):
            row[j] = row[j] + row[j - 1]
        row.append(1)


vyska = int(input("Zadajte výšku Pascalovho trojuholníka: "))
pascalov_trojuholnik(vyska)
