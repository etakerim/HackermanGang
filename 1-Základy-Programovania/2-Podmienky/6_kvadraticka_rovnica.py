import math


a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if a == 0:
    print("Ide o lineárnu rovnicu")

else:
    print(f"\n{a:g}x² + {b:g}x + {c:g} = 0")

    D = b ** 2 - 4 * a * c

    if D < 0:
        print("Kvadratická rovnica nemá riešenie v R")

    else:
        if D > 0:
            x1 = (-b - math.sqrt(D)) / (2 * a)
            x2 = (-b + math.sqrt(D)) / (2 * a)
            print(f"x₁ = {x1}")
            print(f"x₂ = {x2}")

        elif D == 0:
            x = -b / (2 * a)
            print(f"x = {x}")

        Vx = -b / (2 * a)
        Vy = c - ((b ** 2) / (4 * a))
        print(f"V[{Vx}; {Vy}]")
