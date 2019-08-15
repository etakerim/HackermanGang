nazov = input("Názov súboru s článkom: ")

pocet_znakov = 0
pocet_slov = 0
pocet_viet = 0

je_medzera = True
clanok = open(nazov, "r")

for riadok in clanok:
    riadok = riadok.rstrip()

    for znak in riadok:
        pocet_znakov += 1

        if znak == ".":
            pocet_viet += 1

        if znak.isspace():
            je_medzera = True
        elif je_medzera and not znak.isspace():
            pocet_slov += 1
            je_medzera = False

clanok.close()

print(f"Znaky: {pocet_znakov}")
print(f"Slová: {pocet_slov}")
print(f"Vety: {pocet_viet}")
print(f"Normostany: {int(pocet_znakov / 1800)}")
