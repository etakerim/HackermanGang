nazov = input("Názov súboru s článkom: ")

STO_PERCENT = 100
abeceda = [0] * 26
pismena = 0

clanok = open(nazov, "r")

for riadok in clanok:
    for pismeno in riadok:
        if pismeno.isalpha():
            pozicia = ord(pismeno.upper()) - ord("A")
            if pozicia >= 0 and pozicia <= 26:
                abeceda[pozicia] += 1
                pismena += 1
clanok.close()

for i in range(len(abeceda)):
    pismeno = chr(ord("A") + i)
    vyskyt = int(STO_PERCENT * (abeceda[i] / pismena))
    print(f"{pismeno}: {'*' * vyskyt}")
