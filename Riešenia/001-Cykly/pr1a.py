vyska = int(input("vyska: "))

hviezdy = 1
medzery = vyska - 1

for r in range(vyska):
    print(' ' * medzery, end='')
    print('*' * hviezdy)
    hviezdy += 2
    medzery -= 1

for r in range(vyska):
    hviezdy -= 2
    medzery += 1
    print(' ' * medzery, end='')
    print('*' * hviezdy)
    


    

