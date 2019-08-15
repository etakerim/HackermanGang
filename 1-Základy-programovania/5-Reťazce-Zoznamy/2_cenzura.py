vstup = input("Správa: ")
prepis = input("Samohlásku nahraď: ")
vystup = ""

samohlasky = "aeiouyáéíóúý"
najdene = False

for i in range(len(vstup)):
    for j in range(len(samohlasky)):
        if vstup[i] == samohlasky[j]:
            vystup += prepis
            najdene = True
            break

    if not najdene:
        vystup += vstup[i]

    najdene = False

print("Cenzurované", vystup)
