decimal = int(input("Dec: "))
roman = []
miesto = 0
tabulka = [["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],
           ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
           ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]]

while decimal != 0:
    cislo = decimal % 10
    if miesto >= 3:
        for i in range(cislo):
            roman.append("M")
    else:
        roman.append(tabulka[miesto][cislo])

    decimal = decimal // 10
    miesto += 1

roman.reverse()
print("".join(roman))
