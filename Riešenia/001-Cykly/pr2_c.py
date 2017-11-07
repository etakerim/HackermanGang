a = int(input("a: "))
txt = input("slovo: ")
vypln = input("vypln: ")
vata = vypln[0] * len(txt)

for i in range(a):
    for j in range(a):
        if i == 0 or i + 1 == a or j == 0 or (j + 1) == a:
            print(vata, end=' ')
        else:
            print(txt, end=' ')
    print()
