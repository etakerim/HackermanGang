vyska = int(input("Zadaj výšku smaragdu: "))
vyska = vyska // 2
# Berieme do úvahy vždy len polovičnú výšku

# Horná časť
for riadok in range(vyska):
    medzery = vyska - riadok - 1
    hviezdy = 2 * riadok + 1
    print(' ' * medzery + '#' * hviezdy)


# Dolná časť
for riadok in range(vyska):
    medzery = riadok
    hviezdy = 2 * (vyska - riadok) - 1
    print(' ' * medzery + '#' * hviezdy)
