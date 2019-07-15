print("--- KALKULAČKA ---- ")

# Vstupy
cislo1 = float(input("Zadaj prvé číslo: "))
cislo2 = float(input("Zadaj druhé číslo: "))
operator = input("Čo chceš spraviť? (+, -, /, *, **) : ")

# Výpočet
if operator == "+":
    print("{} + {} = {}".format(cislo1, cislo2, cislo1 + cislo2))
elif operator == "-":
    print("{} - {} = {}".format(cislo1, cislo2, cislo1 - cislo2))
elif operator == "*":
    print("{} * {} = {}".format(cislo1, cislo2, cislo1 * cislo2))
elif operator == "/":
    print("{} / {} = {}".format(cislo1, cislo2, cislo1 / cislo2))
elif operator == "**":
    print("{} ** {} = {}".format(cislo1, cislo2, cislo1 ** cislo2))
