odchod = input("Čas: ")
trvanie = input("Trvanie cesty vlakom: ")

odchod = odchod.split(":")
hod = int(odchod[0])
min = int(odchod[1])
odchod = [hod, min]

trvanie = trvanie.split(":")
hod = int(trvanie[0])
min = int(trvanie[1])
trvanie = [hod, min]

vlaky = []
autobusy = []
cp = open("cp.csv", "r")

for spoj in cp:
    spoj = spoj.split(",")
    doprava = spoj[0].strip()

    if doprava == "bus":
        autobusy.append([])

    for cas in spoj[1:]:
        cas = cas.split(":")
        hod = int(cas[0])
        min = int(cas[1])

        if doprava == "vlak":
            vlaky.append([hod, min])
        elif doprava == "bus":
            autobusy[-1].append([hod, min])

print("Najbližší spoj (vlak, autobus):")
nasiel = False

for vlak in vlaky:
    # Nájdi najbližší odchod vlaku
    if (vlak[0] * 60 + vlak[1]) >= (odchod[0] * 60 + odchod[1]):
        # Zisti, kedy prídeme odchod + trvanie = prichod
        min = (vlak[1] + trvanie[1]) % 60
        hod = ((vlak[0] + trvanie[0]) + ((vlak[1] + trvanie[1]) // 60)) % 24
        prichod = [hod, min]

        for linka in autobusy:
            stanica = linka[0]

            # K tomu pozri autobusovú linku, ktorá odchádza zo stanice, do ktorej vlak ide
            if (stanica[0] * 60 + stanica[1]) >= (trvanie[0] * 60 + trvanie[1]):

                for autobus in linka[1:]:
                    # Prestup: Nájdi autobus, ktorý odchádza najskôr po príchode vlaku
                    if (not nasiel and (autobus[0] * 60 + autobus[1]) > (prichod[0] * 60 + prichod[1])):
                        print(f"{vlak[0]:02d}:{vlak[1]:02d} - "
                              f"{prichod[0]:02d}:{prichod[1]:02d}, "
                              f"{autobus[0]:02d}:{autobus[1]:02d} - ")
                        nasiel = True
cp.close()
