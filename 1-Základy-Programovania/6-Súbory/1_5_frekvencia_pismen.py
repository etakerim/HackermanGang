nazov = input("Názov súboru s článkom: ")

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
    vyskyt = 100 * (abeceda[i] / pismena)
    print(f"{pismeno}: {vyskyt:.2f}%")
