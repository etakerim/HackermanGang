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
p_i = -1
ngram = ""

for riadok in korpus:
    riadok = riadok.strip()

    for znak in riadok:
        # Zhromažduj znaky, kým nemáš n-gram požadovanej dĺžky
        ngram += znak
        if len(ngram) != dlzka_ngram:
            continue

        # Poznač si, či sme znak už predtým videli
        if ngram in legenda:
            i = legenda.index(ngram)

            # Ak sme ho videli pripočítaj prechodový stav
            if p_i != -1:
                matica[p_i][i] += 1
                pocty[i] += 1
                p_i = i
        else:
            # Ak sme znak nevideli pridaj preň matici nakoniec prázdny riadok a stĺpec
            p_i = len(legenda)
            legenda.append(ngram)
            pocty.append(1)

            for r in matica:
                r.append(0)
            matica.append([0] * len(legenda))

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
zaciatky = [ngram for ngram in legenda if ngram[0].isupper()]
ngram = random.choice(zaciatky)
text += ngram

for i in range(dlzka_generuj - 1):
    # Nájdi stav, v ktorom sme
    stav = legenda.index(ngram)
    # Podľa pravdepodobností v danom riadku matice vyber stĺpec a tým aj nový ngram
    ngram = random.choices(legenda, weights=matica[stav])[0]
    text += ngram

print(text)
