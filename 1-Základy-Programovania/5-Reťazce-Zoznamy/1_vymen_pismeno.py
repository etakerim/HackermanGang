text = input("Správa: ")
chyba = input("Za chybné písmeno: ")
nahrada = input("Vymeň: ")

upravene = ""
for pismeno in text:
    if pismeno == chyba:
        upravene += nahrada
    else:
        upravene += pismeno

print("\nOpravené!")
print(upravene)
