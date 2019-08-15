nazov_suboru = input("Názov súboru so správou: ")
prepis = input("Samohlásku nahraď: ")

samohlasky = "aeiouyáéíóúý"
najdene = False
print("\nCenzurované:")

subor = open(nazov_suboru, "r")

for riadok in subor:
    riadok = riadok.rstrip()
    vystup = ""

    for i in range(len(riadok)):
        for j in range(len(samohlasky)):
            if riadok[i] == samohlasky[j]:
                vystup += prepis
                najdene = True
                break

        if not najdene:
            vystup += riadok[i]

        najdene = False
    print(vystup)

subor.close()
