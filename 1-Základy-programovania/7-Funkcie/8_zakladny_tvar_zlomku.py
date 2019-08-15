def nsd(a, b):
    # Najväčší spoločný deliteľ
    # alebo: math.gcd(a, b)
    while b > 0:
        a, b = b, a % b
    return a


def nsn(a, b):
    # Najmenší spoločný násobok
    return a * b // nsd(a, b)


def zakladny_tvar(zlomok):
    delitel = nsd(zlomok[0], zlomok[1])
    return [
        zlomok[0] // delitel,
        zlomok[1] // delitel
    ]


def vytvor_zlomok(retazec):
    # alebo: map(int, retazec.split("/"))
    zlomok = retazec.split("/")
    for i in range(len(zlomok)):
        zlomok[i] = int(zlomok[i])
    return zlomok


def nasobit(x, y):
    citatel = x[0] * y[0]
    menovatel = x[1] * y[1]
    zlomok = [citatel, menovatel]
    return zakladny_tvar(zlomok)


def delit(x, y):
    citatel = x[0] * y[1]
    menovatel = x[1] * y[0]
    zlomok = [citatel, menovatel]
    return zakladny_tvar(zlomok)


def scitat(x, y):
    menovatel = nsn(x[1], y[1])
    x_citatel = x[0] * (menovatel // x[1])
    y_citatel = y[0] * (menovatel // y[1])
    citatel = x_citatel + y_citatel
    zlomok = [citatel, menovatel]
    return zakladny_tvar(zlomok)


def odcitat(x, y):
    menovatel = nsn(x[1], y[1])
    x_citatel = x[0] * (menovatel // x[1])
    y_citatel = y[0] * (menovatel // y[1])
    citatel = x_citatel - y_citatel
    zlomok = [citatel, menovatel]
    return zakladny_tvar(zlomok)


def vypis(zlomok):
    return f"{zlomok[0]}/{zlomok[1]}"


print("Kalkulačka zlomkov")
a = input("a = ")
b = input("b = ")
akcia = input("Vypočítaj (+, -, *, /): ")

a = zakladny_tvar(vytvor_zlomok(a))
b = zakladny_tvar(vytvor_zlomok(b))

print("\nVýsledok:")
if akcia == '+':
    print(f"{vypis(a)} + {vypis(b)} = {vypis(scitat(a, b))}")
elif akcia == '-':
    print(f"{vypis(a)} - {vypis(b)} = {vypis(odcitat(a, b))}")
elif akcia == '*':
    print(f"{vypis(a)} * {vypis(b)} = {vypis(nasobit(a, b))}")
elif akcia == '/':
    print(f"{vypis(a)} / {vypis(b)} = {vypis(delit(a, b))}")
