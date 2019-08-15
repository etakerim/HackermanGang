nazov_suboru = input("Názov súboru so správou: ")
chyba = input("Za chybné písmeno: ")
nahrada = input("Vymeň: ")

subor = open(nazov_suboru, "r")

print("\nOpravené!")

for riadok in subor:
    riadok = riadok.rstrip()
    upravene = ""

    for pismeno in riadok:
        if pismeno == chyba:
            upravene += nahrada
        else:
            upravene += pismeno
    print(upravene)

subor.close()
