nazov = input("Rečnícky prejav: ")
prejav = open(nazov, "r")

slovo = ""
najdlhsie = ""

for riadok in prejav:
    for znak in riadok:
        if znak.isalpha():
            slovo += znak
        else:
            if len(slovo) > len(najdlhsie):
                najdlhsie = slovo
            slovo = ""

print(f"Najdlhšie slovo v ňom: {najdlhsie}")
prejav.close()
