vklad = float(input("Vklad v €: "))
sadzba = float(input("Úroková sadzba p.a. v %: "))
urocenie = input("Typ úročenia (jednoduché / zložené): ")
ciel = float(input("Žiadaná suma v €: "))

sadzba /= 100
rok = 0
suma = vklad

if urocenie == "jednoduché":
    urok = vklad * sadzba
if urocenie == "zložené":
    sadzba += 1
    povodna_sadzba = sadzba

print(f"{'Mesiac':10s} {'Suma':15s} {'Úrok':10s}")

while suma < ciel:
    if urocenie == "jednoduché":
        suma += urok
    elif urocenie == "zložené":
        urok = suma * (sadzba - 1)
        suma = vklad * sadzba
        sadzba *= povodna_sadzba
    else:
        break
    rok += 1
    print(f"{rok:10d} {suma:15.2f} {urok:10.2f}")
