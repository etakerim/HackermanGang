def rimske_na_arabske(rimske):
    TABULKA = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    arabske = []
    vysledok = 0

    for symbol in rimske:
        arabske.append(TABULKA[symbol])

    i = 0
    while i < len(arabske):
        if i + 1 != len(arabske) and arabske[i] < arabske[i + 1]:
            vysledok += arabske[i + 1] - arabske[i]
            i += 2
        else:
            vysledok += arabske[i]
            i += 1

    return vysledok


cislo = input("Zadaj rímske číslo: ")
print(rimske_na_arabske(cislo))
