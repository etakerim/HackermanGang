retazec = input()
akronym = ""

# Pridať prvé písmeno do výstupu
akronym = retazec[0].upper()
prev = retazec[0]

# for - Prejsť celým reťazcom
for z in range(1, len(retazec)):
    # Po medzere pridať nové písmeno (veľké) do výstupu (akronymu)
    if prev == " " and retazec[z] != " ":
        akronym += retazec[z].upper()
    prev = retazec[z]

print(akronym)
        
    
