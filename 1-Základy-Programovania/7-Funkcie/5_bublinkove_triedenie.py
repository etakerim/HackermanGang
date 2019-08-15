def bublinkove_triedenie(zoznam, stlpec):
    for i in range(len(zoznam) - 1):
        for j in range(len(zoznam) - i - 1):
            if zoznam[j][stlpec] > zoznam[j + 1][stlpec]:
                x = zoznam[j]
                zoznam[j] = zoznam[j + 1]
                zoznam[j + 1] = x


subor = open("ziaci.csv", "r")
hlavicka = []
ziaci = []

for riadok in subor:
    riadok = riadok.strip()
    if not hlavicka:
        hlavicka = riadok.split(",")
    else:
        ziaci.append(riadok.split(","))

subor.close()

kriterium = input("Triediť podľa stĺpca: ")
stlpec = 0

for i in range(len(hlavicka)):
    if hlavicka[i].strip() == kriterium:
        stlpec = i

bublinkove_triedenie(ziaci, stlpec)
for nadpis in hlavicka:
    print(f"{nadpis:20s}", end=":")
print()

for ziak in ziaci:
    for nadpis in ziak:
        print(f"{nadpis:20s}", end=":")
    print()
