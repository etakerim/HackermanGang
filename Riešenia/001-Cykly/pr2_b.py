a = int(input("a: "))
txt = input("slovo: ")
vypln = input("vypln: " ) 
vata = vypln[0] * len(txt)

for i in range(a):
    for j in range(a):
        if i == j or (a - i - 1) == j:
            print(vata, end=' ')
        else:
            print(txt, end=' ')
    print()
