import sys
import random

bane = random.randint(5, 8)
ludia = random.randint(40, 100)
peniaze = random.randint(10, 60) * ludia
tazba = random.randint(80, 120)

sklad_ruda = 0
koef_spokoj = 1

for rok in range(1, 11):
    cena_bane = random.randint(2000, 4000)
    cena_rudy = random.randint(7, 19)
    sklad_ruda += sklad_ruda + tazba * bane

    # Situácia v baniach na začiatku roku
    print("\n\n\t{}.ROK".format(rok))
    print("Osada má {} obyvateľov. Koeficient spokojnosti je {:.1f}.".format(ludia, koef_spokoj))
    print("Vlastníte {} baní. Z každej z nich sa vyťaží {} ton rudy.".format(bane, tazba))
    print("Zásoba rudy je {} ton.".format(sklad_ruda))

    # Hráčove rozhodnutia - PREDAJ
    print("\n\nPREDAJ")
    print("Cena za tonu rudy je " + str(cena_rudy))
    print("Cena bane je " + str(cena_bane))

    while True:
        predaj = int(input("Koľko rudy predáš?: "))
        if predaj >= 0 and predaj <= sklad_ruda:
            sklad_ruda -= predaj            # Odober rudu zo skladu
            peniaze += predaj * cena_rudy   # Započítaj zisk z predaja
            break
    
    while True:
        predaj = int(input("Koľko baní predáš?: "))
        if predaj >= 0 and predaj < bane:
            bane -= predaj
            peniaze += predaj * cena_bane
            break
    print("\nMáš {} peňazí.\n".format(peniaze))


    # Hráčové rozhodnutia - NÁKUP
    print("\n\nNÁKUP")
    while True:
        nakup = int(input("Koľko minieš na potraviny?: "))
        if nakup >= 0 and nakup <= peniaze:
            peniaze -= nakup
            break
        
    # Uprav koeficient spokojnosti
    if nakup / ludia > 100:
        koef_spokoj += 0.1
    elif nakup / ludia < 50:
        koef_spokoj -= 0.2

    # Nákup nových baní
    while True:
        nakup = int(input("Koľko nových baní kúpiš?: "))
        if nakup >= 0 and (nakup * cena_bane) <= peniaze:
            peniaze -= (nakup * cena_bane)
            bane += nakup
            break

    if koef_spokoj > 1.1:
        tazba += random.randint(1, 20)
        ludia += random.randint(1, 10)
    elif koef_spokoj < 0.9:
        tazba -= random.randint(1, 20)
        ludia -= random.randint(1, 10)
    elif koef_spokoj < 0.6:
        print("Baníci sa vzbúrili! --- PREHRA ----")
        sys.exit()

    if ludia / bane < 8:
        print("Baníci sú prepracovaní! -- PREHRA ----")
        sys.exit()
    if ludia < 30:
        print("Zostalo málo baníkov! -- PREHRA ----")
        sys.exit()

    if random.random() < 0.01:
        print("Rádioaktívne žiarenie zahynulo veľa ľudí!")
        ludia //= 2

    if tazba >= 150:
        print("Trh je nasýtení! Zníži sa ťažba rudy.")
        tazba //=2

print("Vo funkcii si obstál úspšne! --- VÝHRA ----") 
