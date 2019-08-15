x = int(input("1.číslo: "))
y = int(input("2.číslo: "))
z = int(input("3.číslo: "))

najviac = x
poradie = 1

if y > najviac:
    najviac = y
    poradie = 2

if z > najviac:
    najviac = z
    poradie = 3

print(f"Najväčie je {poradie}.číslo a to je {najviac}.")
