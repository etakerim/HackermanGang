import random

autor = input("Chcem písať ako: ")
dlzka_ngram = int(input("Dĺžka n-gramu: "))
dlzka_generuj = int(input("Počet znakov výsledného textu: "))
dlzka_generuj //= dlzka_ngram

print("Spracúvam korpus tvorby autora ...")
korpus = open(autor.lower() + ".txt", "r")

legenda = []        # Každý nový znak si zaznač do hlavičky tabuľky
pocty = []          # Počet znakov korpusu
matica = []         # Tabuľka výskytov po sebe idúcich dvoch znakov z legendy
pred_pozicia = None
ngram = ""

for riadok in korpus:
    riadok = riadok.strip()

    for znak in riadok:
        # Zhromažduj znaky, kým nemáš n-gram požadovanej dĺžky
        ngram += znak
        if len(ngram) != dlzka_ngram:
            continue

        # Poznač si, či sme znak už predtým videli
        videl = False
        pozicia = 0
        for i in range(len(legenda)):
            if legenda[i] == ngram:
                pozicia = i
                videl = True
                break

        if not videl:
            # Ak sme znak nevideli pridaj preň matici nakoniec prázdny riadok a stĺpec
            pred_pozicia = len(legenda)
            legenda.append(ngram)
            pocty.append(1)

            for r in matica:
                r.append(0)
            nuly = []
            for i in range(len(legenda)):
                nuly.append(0)
            matica.append(nuly)

        else:
            # Ak sme ho videli pripočítaj prechodový stav
            if pred_pozicia != None:
                matica[pred_pozicia][pozicia] += 1
                pocty[pozicia] += 1
                pred_pozicia = pozicia

        ngram = ""
korpus.close()

print("Spočítavam maticu prechodových stavov ...")
# Normalizuj: premen početnosť na pravdepodobnosť
for r in range(len(matica)):
    for s in range(len(matica[r])):
        matica[r][s] /= pocty[r]


print("Generujem originálny text ...")
text = ""

# Vyber z možných začiatkov začinajúcich veľkým písmenom
zaciatky = []
for retazec in legenda:
    if retazec[0].isupper():
        zaciatky.append(retazec)


vyber = random.randint(0, len(zaciatky) - 1)
ngram = zaciatky[vyber]
text += ngram

# Nájdi stav, v ktorom sme na začiatku
stav = 0
for i in range(len(legenda)):
    if legenda[i] == ngram:
        stav = i
        break


for i in range(dlzka_generuj - 1):
    # Podľa pravdepodobností v danom riadku matice vyber stĺpec a tým aj nový ngram
    uroven = 1.0
    p = random.random()
    # https://stackoverflow.com/questions/3679694/a-weighted-version-of-random-choice
    for j in range(len(matica[r])):
        vaha = matica[stav][j]
        p -= vaha
        if p < vaha:
            ngram = legenda[j]
            stav = j
            text += ngram
            break

print(text)
