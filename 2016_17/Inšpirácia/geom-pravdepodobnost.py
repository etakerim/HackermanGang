"""
    Výpočet geometrickej pravdepodobnosti 
    stretnutia dvoch osôb v danom časovom intervale
    (okne) ak sa čakajú nejaký interval
"""
import sys
import math

def pravdepodb_stretnutia(cas_celkom, cas_caka):
    a = math.hypot(cas_celkom - cas_caka, cas_celkom - cas_caka)
    b = math.hypot(cas_caka, cas_caka)
    plocha_stret = ((cas_caka ** 2) + (a * b))   
    spolu_plocha = cas_celkom ** 2
    
    if spolu_plocha == 0:
        return 0
    else:
        return (plocha_stret / spolu_plocha) * 100

def simuluj(filename):
    with open(filename, mode="w") as fw: 
        for hodintv in range(1, 24):
            for cakanie in range(hodintv * 60):
                p = pravdepodb_stretnutia(hodintv * 60, cakanie)
                msg = ("{:4f}, ".format(p)).replace(".", ",")
                fw.write(msg)
            fw.write("\n")


def uzivatel():
    try:
        t1 = int(input("A Hodina (0 - 24): "))
        t2 = int(input("B Hodina (0 - 24): "))
        t_pocka = int(input("Čakací interval (min): "))

    except TypeError:
        print("Zadaní vstup nie je číslom")
        sys.exit()

    if (0 < t1 or 0 < t2):
        print("Hodiny nie sú v povolenom rozsahu!")
        sys.exit()

    tmin_spolu = abs(t1 - t2) * 60
    p = pravdepodb_stretnutia(tmin_spolu, t_pocka)
    print("Pravdepodobnosť stretnutia je {:.4f}%".format(p))

if __name__ == "__main__":
    simuluj("geompravdepo.csv")
