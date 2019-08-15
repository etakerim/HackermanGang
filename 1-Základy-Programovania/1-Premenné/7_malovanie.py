# Získaj z klávesnice rozmery miestnosti
print("Rozmery miestnosti")
dlzka = input("Dĺžka (cm): ")
sirka = input("Širka (cm): ")
vyska = input("Výška (cm): ")

# Premeň z písmen na čísla
dlzka = int(dlzka)
sirka = int(sirka)
vyska = int(vyska)

# Získaj z klávesnice rozmery okna a výdatnosť farby
print("Rozmery okna")
okno_sirka = input("Širka (cm): ")
okno_vyska = input("Výška (cm): ")
vydatnost = input("Výdatnosť farby (m²/kg): ")

# Premeň z písmen na čísla
okno_sirka = int(okno_sirka)
okno_vyska = int(okno_vyska)
vydatnost = float(vydatnost)

# Spočítaj plochy stien, stropu a odpočítaj plochu okna
S_miestnost = (dlzka * sirka) + 2 * (vyska * sirka) + 2 * (vyska * dlzka)
S_okno = okno_sirka * okno_vyska

S = (S_miestnost - S_okno) / 10000
kg_farba = S / vydatnost

print(f"Maľovať budeš plochu {S:.2f} m². Kúp {kg_farba:.2f} kg farby.")
