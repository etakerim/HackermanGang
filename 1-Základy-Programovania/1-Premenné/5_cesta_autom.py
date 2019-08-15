km = input("Dĺžka cesty (km): ")
odchod = input("Odchod z domu (hodina): ")
prichod = input("Príchod do hotela (hodina): ")

km = float(km)
odchod = int(odchod)
prichod = int(prichod)

hod = prichod - odchod
print(f"Pôjdete priemerne {km / hod:.2f} km/h.")
