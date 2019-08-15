def sifruj(sprava, kluc):
    sifra = ""
    A = ord("A")
    Z = ord("Z")
    ABECEDA = Z - A + 1
    sprava = sprava.upper()

    for i in range(len(sprava)):
        pismeno = sprava[i]
        k = kluc[i % len(kluc)]

        if A <= ord(pismeno) <= Z:
            poradie = ord(pismeno) - A
            posun = ord(k) - A

            poradie = (poradie + posun) % ABECEDA
            sifra += chr(poradie + A)

    return sifra


def desifruj(sifra, kluc):
    sprava = ""
    A = ord("A")
    Z = ord("Z")
    ABECEDA = Z - A + 1
    sifra = sifra.upper()

    for i in range(len(sifra)):
        pismeno = sifra[i]
        k = kluc[i % len(kluc)]

        if A <= ord(pismeno) <= Z:
            poradie = ord(pismeno) - A
            posun = ord(k) - A

            poradie = (poradie - posun) % ABECEDA
            sprava += chr(poradie + A)

    return sprava


retazec = input("Zadaj správu: ")
kluc = input("Vlož tajný kľúč: ")
akcia = input("Čo spraviť (šifruj / dešifruj): ")
s = ""

if akcia == "šifruj":
    print("Zašifrovaná správa: ", end="")
    s = sifruj(retazec, kluc)

elif akcia == "dešifruj":
    print("Dešifrovaná správa: ", end="")
    s = desifruj(retazec, kluc)

print(s)
