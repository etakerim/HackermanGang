#Funkciu priemer, param:pole, vystup:priemer
def priemer(zozcis):
    apriem = 0
    for i in range(len(zozcis)):
        apriem += zozcis[i]

    return apriem / len(zozcis)


# Hlavny program
# cisla = [for x in input().split(" ")]
cisla = [1, 2, 3, 4, 5, 6]
print("Priemer: ", priemer(cisla))
