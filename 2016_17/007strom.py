"""
 Kreslenie stromu
 -> dôležité je uvedomiť vzťahy (vzory) medzi veličinami
 (nakresliť) inak je tento problém veľmi ťažký

"""
vyska = int(input("Zadajte výšku stromu: "))
medzery = vyska - 2
hviezdy = 1
stred = medzery

for i in range(vyska - 1):

    for j in range(medzery):
        print(" ", end="")

    for j in range(hviezdy):
        print("*", end="")

    print()    # Vytlačí nový riadok
    medzery -= 1
    hviezdy += 2

for i in range(stred):
    print(" ", end="")
print("*")
