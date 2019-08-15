nazov = input("Nákupný košík je v súbore: ")

riadok = "+" + 20 * "-" + "+" + 15 * "-" + "+" + 15 * "-" + "+"
print(riadok)
print(f"|{'Tovar':20s}|{'DPH':15s}|{'Cena s DPH':15s}|")

celkom = 0
nakup = open(nazov, "r")

for polozka in nakup:
    polozka = polozka.rstrip()
    polozka = polozka.split(",")

    if len(polozka) == 2:
        tovar = polozka[0]
        cena = float(polozka[1])
        celkom += cena
        print(riadok)
        print(f"|{tovar:20s}|{cena * 0.2:15.2f}|{cena:15.2f}|")

nakup.close()

print(riadok)
print(f"|{'CELKOM':20s}|{celkom * 0.2:15.2f}|{celkom:15.2f}|")
print(riadok)
