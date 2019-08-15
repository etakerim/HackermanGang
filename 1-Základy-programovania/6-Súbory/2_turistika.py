nazov = input("Výškový profil trasy je v súbore: ")

ROVINA_KMH = 3.6
KROK_M = 10

predch_vyska = None
vzdialenost_m = 0
trvanie_min = 0

celkom_stupanie = 0
celkom_klesanie = 0

najvyssie = None
najnizsie = None

trasa = open(nazov, "r")

for miesto in trasa:
    nadmorska_vyska = int(miesto)
    vzdialenost_m += KROK_M

    # Ak neexistuje predošlá nadmorská výška, tak sme neprešli žiaden úsek
    if predch_vyska != None:
        stupanie = nadmorska_vyska - predch_vyska

        # Zisti, či sme dosiahli rekordnú nadmorskú výšku a zaznamenaj si ju.
        if najvyssie == None or nadmorska_vyska > najvyssie:
            najvyssie = nadmorska_vyska
        elif najnizsie == None or nadmorska_vyska < najnizsie:
            najnizsie = nadmorska_vyska

        # Zobrazenie vzdialenosti medzi dvomi miestami zo svahu do roviny.
        # Pri stúpaní prejdeme za rovnaký čas akoby kratšiu vzdialenosť, preto
        # sa prepona zobrazí do dolnej odvesy a pri klesaní naopak
        if stupanie > 0:
            rovina_vzd = KROK_M ** 2 - stupanie ** 2
            celkom_stupanie += stupanie

        elif stupanie < 0:
            rovina_vzd = KROK_M ** 2 + stupanie ** 2
            celkom_klesanie += abs(stupanie)

        else:
            rovina_vzd = KROK_M

        # Čas na prejdenie medzi miestami v minútach
        trvanie_min += ((rovina_vzd / 1000) / ROVINA_KMH) * 60

    predch_vyska = nadmorska_vyska

trasa.close()

print(f"Trasa: {vzdialenost_m / 1000:.3f} km - "
      f"{int(trvanie_min // 60)} h {int(trvanie_min % 60)} min")
print(f"Stúpanie: {celkom_stupanie} m")
print(f"Klesanie: {celkom_klesanie} m")
print(f"Najnižšie miesto trasy: {najnizsie} m")
print(f"Najvyššie miesto trasy: {najvyssie} m")
