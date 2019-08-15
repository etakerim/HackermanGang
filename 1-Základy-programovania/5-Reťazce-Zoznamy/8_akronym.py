veta = input("Slovné spojenie: ")
skratka = ""
je_medzera = True

for znak in veta:
    if znak.isspace():
        je_medzera = True
    elif je_medzera and znak.isalpha():
       je_medzera = False
       skratka += znak.upper()

print(f"Skratka: {skratka}")
