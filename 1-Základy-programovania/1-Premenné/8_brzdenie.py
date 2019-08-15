import math


M_CLOVEK = 80

print("Vlaková súprava")

v = int(input("- Rýchlosť (km/h): "))
lokomotiva = float(input("- Hmotnosť lokomotívy (t): "))
vagon = float(input("- Hmotnosť vagóna (t): "))

pocet_vagonov = int(input("- Počet vagónov: "))
pocet_cestujucich = int(input("- Počet miest na vagón: "))
naplnenie = int(input("- Zaplnenosť vlaku (%): "))
F_b = int(input("- Brzdná sila (N/t): "))

# Premeň jednotky na základné SI
v /= 3.6
lokomotiva *= 1000
vagon *= 1000
F_b /= 1000

# Hmotnosť súpravy je hmotnosť lokomotívy, všetkých vagónov a ľudí
m = (lokomotiva +
     (pocet_vagonov * vagon) +
     M_CLOVEK * (pocet_vagonov * pocet_cestujucich) * (naplnenie / 100))

# Vypočítaj celkovú kinetickú energiu, tá je rovnaká ako práca
# ktorú musia brzdy vykonať na zabrzdenie.
W = 0.5 * m * (v ** 2)

# Celková sila pôsobiaca proti pohybu vlaku
F = F_b * m

# Z definície práce W = F * s, vypočítaj dráhu potrebnú na zastavenie
s = W / F

# Vypočítaj čas potrebný na zastavenie pre rovnomerný spomalený pohyb
a = F / m
t = math.sqrt(2 * s / a)

print(f"V rýchlosti {int(v * 3.6)} km/h zabrzdí súprava s hmotnosťou "
      f"{int(m / 1000)} t na vzdialnosť {int(s)} m a bude to "
      f"trvať {int(t)} s.")
