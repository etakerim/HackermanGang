clanok = input("Článok: ")

abeceda = [0] * 26
pismena = 0

for pismeno in clanok:
    if pismeno.isalpha():
        pozicia = ord(pismeno.upper()) - ord("A")
        if pozicia >= 0 and pozicia <= 26:
            abeceda[pozicia] += 1
            pismena += 1

for i in range(len(abeceda)):
    pismeno = chr(ord("A") + i)
    vyskyt = 100 * (abeceda[i] / pismena)
    print(f"{pismeno}: {vyskyt:.2f}%")
