from datetime import datetime
from datetime import timedelta

odchod = datetime.strptime(input("Čas: "), "%H:%M")
cesta = datetime.strptime(input("Trvanie cesty vlakom: "), "%H:%M")
trvanie = timedelta(hours=cesta.hour, minutes=cesta.minute)

vlaky = []
autobusy = []
cp = open("cp.csv", "r")

for spoj in cp:
    spoj = spoj.split(",")
    doprava = spoj[0].strip()

    if doprava == "bus":
        autobusy.append([])

    for cas in spoj[1:]:
        cas = datetime.strptime(cas.strip(), "%H:%M")

        if doprava == "vlak":
            vlaky.append(cas)
        elif doprava == "bus":
            autobusy[-1].append(cas)

print("Najbližší spoj (vlak, autobus):")
nasiel = False

for vlak in vlaky:
    # Nájdi najbližší odchod vlaku
    if vlak >= odchod:
        # Zisti, kedy prídeme odchod + trvanie = prichod
        prichod = vlak + trvanie

        for linka in autobusy:
            stanica = linka[0]
            # K tomu pozri autobusovú linku, ktorá odchádza zo stanice, do ktorej vlak ide
            if stanica >= cesta:
                for autobus in linka[1:]:
                    # Prestup: Nájdi autobus, ktorý odchádza najskôr po príchode vlaku
                    if not nasiel and autobus > prichod:
                        print(f"{vlak.strftime('%H:%M')} - "
                              f"{prichod.strftime('%H:%M')}, "
                              f"{autobus.strftime('%H:%M')} - ")
                        nasiel = True

cp.close()
