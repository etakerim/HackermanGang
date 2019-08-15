n = int(input("Počet riadkov a stĺpcov: "))
slovo = input("Opakovať slovo: ")
ram = len(slovo) * "#"

for riadok in range(n):
    for stlpec in range(n):
        if riadok == 0 or stlpec == 0 or riadok == n - 1 or stlpec == n - 1:
            print(ram, end=" ")
        else:
            print(slovo, end=" ")
    print()
