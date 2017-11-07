a = int(input("Strana štvorca: "))
txt = input("Slovo do mriežky: ")

for i in range(a):
    for j in range(a):
        print(txt, end=' ')
    print()
