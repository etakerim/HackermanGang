#qrencode -ofile.png < vstup.txt
import random
import unicodedata

def odstran_diakritiku(retazec):
    vystup = []
    for znak in unicodedata.normalize("NFD", retazec):
        if unicodedata.category(znak) != "Mn":
            vystup.append(znak)
    
    return "".join(vystup)

def cezarova_sifra(retazec, kluc, desifrujes):
    vystup = []
    zaklad = ord(" ")
    koniec = ord("~")
    limit = koniec - zaklad
    
    random.seed(kluc)
    posun = random.randint(-0x1A, 0x1A)
    if desifrujes:
        posun = -posun
    
    for znak in reversed(list(retazec)):
        if ord(znak) >= zaklad and ord(znak) <= koniec:
            vystup.append(chr(((ord(znak) - zaklad + posun) % limit) + zaklad))
        else:
            vystup.append(znak)

    return "".join(vystup)


KLUC = 0x123A7B97CF26

print("------- JEDNODUCHE SIFROVANIE ------------- ")
print("[1]\tZasifruj")
print("[2]\tOdsifruj")
volba = int(input("Zadajte volbu (1 - 2): "))
nazovsuboru = input("Zadajte nazov suboru: ")

vstup = ""
with open(nazovsuboru, mode="r") as subor:
    for line in subor:
        vstup += line

if volba == 1:
    vystup = cezarova_sifra(odstran_diakritiku(vstup), KLUC, False) 
elif volba == 2:
    vystup = cezarova_sifra(vstup, KLUC, True)
    
print("Vystup:",  vystup)
