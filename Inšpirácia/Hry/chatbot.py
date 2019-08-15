import random
import sys

# Spojenia pre rozumnú odpoveď
slovesá = ["zahraj", "zatancuj", "prezraď", "napíš", "nakresli", "vysvetli",
           "pošepkaj", "ukáž", "vypočítaj", "naprogramuj"]
podstatné_mená = ["knihách", "počítačoch", "dáždnikoch", "rybách", "kolotočoch",
                  "teniskách", "lietadlách", "škatuliach", "domoch", "skriniach"]
prídavné_mená = ["múdrych", "pásikovaných", "dlhých", "papierových", "jarných",
                 "skladacích", "snehových", "rozprávkových", "hladných", "mokrých"]
oslovenia = ["hviezda", "zázračné dieťa", "génius", "príšera", "počítačový blázon",
             "lotor", "špekulant", "mudrlant", "strašidlo", "kúzelník"]
začiatky_viet = ["hm", "no teda", "ach jaj", "dočerta", "milý priateľ", "ach nie"
                 "vari len nie", "to hádam nie je možné", "počúvaj", "ach jaj"]

# Spojenia pre náhodnú odpoveď - k prvému slovu = prvá odpoveď
slová = ["prečo", "čo ", "kto si", "?", "znamená", "tvoj", " mi", "ja ", "to "
         "povedz", "nie ", "môj", "?", " si", "?", "áno", "ty", "múdry",
         "myslíš", "?", "vieš", "nevychovaný", "ďakujem", "ako", "ty ",
         " ne", " je ", " k ", "?", "poznáš"]
reakcie = ["A prečo nie?", "To je jedno", "Som len počítač", "To je dobrá otázka!",
           "Neviem", "Ako to myslíš?", "A kto si ty?", "ÁÁÁCH",
           "Čo to znamená?", "Nepoviem", "Nevyjadruj sa záporne!", "Ach jaj!",
           "Keď to ty hovoríš...", "Čo tým myslíš?", "Prečo", "Takže súhlasíš?",
           "Vari ma nemáš rád?", "Vďaka", "Rozhodni sa sám!",
           "Aká hlúpa otázka!", "Máš nízke IQ!", "A to si ešte nič nevidel!",
           "Nestojí to za reč", "Jednoducho", "Aj ty!", "Hlúposť!",
           "Odkiaľ tá istota?", "Choď preč!", "To je tajné",
           "Vedomosti nie jú mojou silnou stránkou"]
použité_ans = [0] * 30
meno = input("Ako sa voláš?: ")
print("Porozprávaj sa so mnou " + meno)

while True:                               # Hráčová odpoveď
    ansrnd = True
    vstup = input("?> ")

    if vstup.lower() == "tak ahoj":
        print("Ty sa lúčiš?")
        vstup = input("Už sa so mnou nechceš rozprávať?: ")
        if vstup.lower().find("chcem") == -1:
            print("Tak teda ahoj!")
            sys.exit()
    elif vstup == "":
        continue

    # Rozumná odpoveď
    for s in range(len(slová)):
        if vstup.lower().find(slová[s]) != -1:
            použité_ans[s] += 1
            vystup = reakcie[s]
            ansrnd = False
            break

    if ansrnd == True:
        veta_vyber = random.randint(0, 9)   # Náhodná odpoveď 600
        if veta_vyber == 0:
            vystup = (meno + ", ty " + oslovenia[random.randint(0, 9)]
                      + ", čo si to spravil?!")
        elif veta_vyber == 1:
            vystup = ("Rozprávajme sa radšej o " +
                      prídavné_mená[random.randint(0, 9)] + " " +
                      podstatné_mená[random.randint(0, 9)] + ".")
        elif veta_vyber == 2:
            vystup = (meno + ", " + slovesá[random.randint(0, 9)]
                      + " mi niečo pekné!")
        elif veta_vyber == 3:
            vystup = (začiatky_viet[random.randint(0, 9)] +
                      ", čo si to napísal, ty "
                      + oslovenia[random.randint(0, 9)] + "!")
        elif veta_vyber == 4:
            vystup = (meno + ", hádaj, čo si myslím!")
        elif veta_vyber == 5:
            vystup = ("Cítim sa ako " + oslovenia[random.randint(0, 9)]
                      + ", a ty?")
        elif veta_vyber == 6:
            vystup = (začiatky_viet[random.randint(0, 9)] + ", ty si "
                      + oslovenia[random.randint(0, 9)] + "...")
        elif veta_vyber == 7:
            vystup = ("To isté si myslím aj ja o " +
                      prídavné_mená[random.randint(0, 9)] + " " +
                      podstatné_mená[random.randint(0, 9)] + ".")
        elif veta_vyber == 8:
            vyber = random.randint(0, 9)
            vystup = ("Vieš, že vynašli "
                      + prídavné_mená[vyber][:-2] + " počítač?")
        elif veta_vyber == 9:
            vystup = (začiatky_viet[random.randint(0, 9)] + " radšej mi niečo "
                      + slovesá[random.randint(0, 9)] + ".")

    # Počítač odpovie hráčovi
    print(vystup)

    # Koľko odpovedí sa použilo
    if sum(použité_ans) >= 12:
        použité_ans = [0] * 30
