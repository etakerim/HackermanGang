prejav = input("Rečnícky prejav: ")

slovo = ""
najdlhsie = ""

for znak in prejav:
    if znak.isalpha():
        slovo += znak
    else:
        if len(slovo) > len(najdlhsie):
            najdlhsie = slovo
        slovo = ""

print(f"Najdlhšie slovo v ňom: {najdlhsie}")
