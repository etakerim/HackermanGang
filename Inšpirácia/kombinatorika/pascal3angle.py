height = int(input('Zadajte vysku Pascalovho trojuholnika: '))
row = [1, 1]
spaces = height
pocet = 0

for i in range(height):
    pocet += 1
    spaces -= 1

    print(' ' * spaces, end='')
    print(' '.join(str(x) for x in row[:pocet]))

    for j in range(pocet - 1,  0, -1):
        row[j] = row[j] + row[j - 1]
    row.append(1)
