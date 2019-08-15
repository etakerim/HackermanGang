nakup = []

while True:
    tovar = input("Čo kúpiť?: ")

    if tovar == "HOTOVO":
        break

    cena = float(input(f"Cena {tovar}?: "))
    nakup.append([tovar, cena])

riadok = "+" + 20 * "-" + "+" + 15 * "-" + "+" + 15 * "-" + "+"
print(riadok)
print(f"|{'Tovar':20s}|{'DPH':15s}|{'Cena s DPH':15s}|")

celkom = 0

for polozka in nakup:
    tovar = polozka[0]
    cena = polozka[1]
    celkom += cena
    print(riadok)
    print(f"|{tovar:20s}|{cena * 0.2:15.2f}|{cena:15.2f}|")


print(riadok)
print(f"|{'CELKOM':20s}|{celkom * 0.2:15.2f}|{celkom:15.2f}|")
print(riadok)
