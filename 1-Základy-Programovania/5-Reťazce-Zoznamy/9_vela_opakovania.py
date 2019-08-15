cesta = input("Cesta robota: ")
skratene = ""

smer = ""
n = 0

for krok in cesta:
    if krok.isalpha():
        if smer == "":
            smer = krok
            n = 1
        elif krok != smer:
            skratene += f"{n}{smer}"
            smer = krok
            n = 1
        else:
            n += 1
skratene += f"{n}{smer}"

print(f"Skomprimované: {skratene}")
