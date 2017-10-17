# Náhodné generovanie DNA zadanej dĺžky z písmen A,C,T,G
import random
import sys

# Táto funkcia príma dva argumenty (retazec dna/rna a indikacia co dostala(True je dna,
# False je rna). V tele funkcie (odsadená časť za dvojbodkou bloku def) si vytvára lokálne
# premenné viditeľné len v nej (nazýva sa to oblasť platnosti = scope). Preto je možné aby hlavný
# program aj funkcie mali premenné s rovnakými názvami, ktoré sú medzi sebou neviditeľné.
# Navratová hodnota prepis() je opačný (komplementárny) reťazec k pôvodnému.
def prepis(dna, je_dna):
    dna2 = ""
    for i in range(len(dna)):
        # Neskorší update : znak = dna[i].upper()
        if dna[i] == "C":
            dna2 += "G"
        elif dna[i] == "G":
            dna2 += "C"
        elif dna[i] == "T":
            dna2 += "A"
        elif dna[i] == "U":
            dna2 += "A"
        elif dna[i] == "A":
            if je_dna:
                dna2 += "T"
            else:
                dna2 += "U"
    return dna2

# ----- Hlavny program ---------------------------------------
# Vstup
dlzka = int(input("DNA Program - Zadaj dĺžku reťazca: "))

if dlzka % 3 != 0:
    print("Neplatný počet dusíkatých báz pre tvorbu tripletov!")
    sys.exit()

# Vygenerujte náhodnú postupnosť písmen A,C,T,G zadanej dlzky
dna = ""
bazy = ["A","C","G","T"]

for i in range(dlzka):
    dna += random.choice(bazy)

print("DNA:  " + dna)

# Prepis z DNA1 do DNA2
dnareplik = prepis(dna, True)   # Volanie našej vlastnej funkcie :)
print("DNA2: " + dnareplik)
