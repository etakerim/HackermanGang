print("Som hovorica kalkulačka a rada počítam!")
a = int(input("Povedz mi prvé číslo: "))
b = int(input("Potrebujem ďašie číslo: "))
cinnost = input("Chceš ich sčítať alebo odčítať: ")

if cinnost == "sčítať":
    print(f"Výsledok tvojho príkladu: {a} plus {b} je {a + b}")
elif cinnost == "odčítať":
    print(f"Výsledok tvojho príkladu: {a} mínus {b} je {a - b}")
else:
    print(f"Neviem čo znamená '{cinnost}'")
