nazov = input("Slovné spojenie je v súbore: ")
je_medzera = True
subor = open(nazov, "r")

for veta in subor:
    skratka = ""
    for znak in veta:
        if znak.isspace():
            je_medzera = True
        elif je_medzera and znak.isalpha():
            je_medzera = False
            skratka += znak.upper()
    print(skratka)
subor.close()
