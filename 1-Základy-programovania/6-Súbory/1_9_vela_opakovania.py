nazov = input("Názov súboru s cestou robota: ")
nazov_skratene = input("Názov súboru pre skrátený zápis cesty: ")

cesta = open(nazov, "r")
skratene = open(nazov_skratene, "w")

smer = ""
n = 0

for riadok in cesta:
    for krok in riadok:
        if krok.isalpha():
            if smer == "":
                smer = krok
                n = 1
            elif krok != smer:
                print(f"{n}{smer}", end="", file=skratene)
                smer = krok
                n = 1
            else:
                n += 1
print(f"{n}{smer}", file=skratene)

cesta.close()
skratene.close()

print(f"Skomprimované v súbore: {nazov_skratene}")
