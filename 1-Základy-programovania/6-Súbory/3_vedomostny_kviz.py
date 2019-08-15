import random

nazov = input("Súbor s kvízovými otázkami: ")
kviz = open(nazov, "r")

otazky = []
skore = 0

# Ulož si pozície otázok v súbore
while True:
    riadok = kviz.readline()
    if not riadok:
        break

    if riadok.startswith("Otázka: "):
        znacka = kviz.tell() - len(riadok)
        otazky.append(znacka)

print("Kvízové otázky pripravené.")
print("Ideme na to!", end="\n\n")

while True:
    # Náhodne vyber otázku
    i = random.randint(0, len(otazky) - 1)
    znacka = otazky[i]
    kviz.seek(znacka)

    # Spýtaj sa otázku a navrhni možnosti
    for riadok in kviz:
        riadok = riadok.rstrip()

        if riadok.startswith("Odpoveď: "):
            odpoved = riadok.lstrip("Odpoveď: ")
            break

        print(riadok.lstrip("Otázka: "))

    # Hráčov tip
    tip = input("Aká je správna odpoveď?: ")
    if tip == odpoved:
        skore += 1
        print(f"Správne! Máš {skore} bodov.\n")
    else:
        print("Nabudúce si to lepšie premysli. Skúsime niečo iné.\n")

kviz.close()
