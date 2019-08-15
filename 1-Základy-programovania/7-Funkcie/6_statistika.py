import math


def priemer(zoznam):
    sucet = 0
    for prvok in zoznam:
        sucet += prvok
    return sucet / len(zoznam)


def modus(zoznam):
    nazvy = []
    vyskyty = []

    # Zisti koľkokrát sa čo vyskytuje
    for prvok in zoznam:
        index = -1
        for i in range(len(nazvy)):
            if prvok == nazvy[i]:
                index = i

        if index != -1:
            vyskyty[index] += 1
        else:
            nazvy.append(prvok)
            vyskyty.append(0)

    # Pozri sa po najväčšom počte objavení sa a prehlás ho za modus
    najviac = None
    rekorder = -1

    for i in range(len(vyskyty)):
        if najviac == None or vyskyty[i] > najviac:
            najviac = vyskyty[i]
            rekorder = i

    return nazvy[rekorder]


def utried(zoznam):
    for i in range(len(zoznam) - 1):
        for j in range(len(zoznam) - i - 1):
            if zoznam[j] > zoznam[j + 1]:
                x = zoznam[j]
                zoznam[j] = zoznam[j + 1]
                zoznam[j + 1] = x


def median(zoznam):
    utried(zoznam)
    stred = (len(zoznam) + 1) // 2
    return zoznam[stred - 1]


def smerodajna_odchylka(zoznam):
    average = priemer(zoznam)

    sucet = 0
    for prvok in zoznam:
        sucet += (prvok - average) ** 2

    return math.sqrt(sucet / len(zoznam))


subor = input("Súbor s bytmi v lokalite: ")
ceny = []
vymery = []

byty = open(subor, "r")

for byt in byty:
    zaznam = byt.split(",")
    ceny.append(int(zaznam[0]))
    vymery.append(int(zaznam[1]))

byty.close()

# Pozri tiež modul "statistics" - https://docs.python.org/3/library/statistics.html
print(f"{'':25s}:{'Cena (€)':15s}:{'Výmera(m^2)':15s}:")
print(f"{'Priemer':25s}:{priemer(ceny):15.2f}:{priemer(vymery):15.2f}:")
print(f"{'Medián':25s}:{median(ceny):15.2f}:{median(vymery):15.2f}:")
print(f"{'Modus':25s}:{modus(ceny):15.2f}:{modus(vymery):15.2f}:")
print(f"{'Smerodajná odchýlka':25s}:{smerodajna_odchylka(ceny):15.2f}:{smerodajna_odchylka(vymery):15.2f}:")
