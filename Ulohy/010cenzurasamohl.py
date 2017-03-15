vstup = input()
vystup = ""

# Určíme samohlásky
samohlasky = "aeiouyáéíóúý"
najdene = False

# Prechádzame r a ak je samohláska prepíšeme
for i in range(len(vstup)):
    for j in range(len(samohlasky)):
        if vstup[i] == samohlasky[j]:
            vystup += "*"
            najdene = True
            break

    if najdene == False:
        vystup += vstup[i]
    najdene = False
    
print(vystup)
