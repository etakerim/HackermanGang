dlzka = input("Dĺžka bazéna (m): ")
sirka = input("Šírka bazéna (m): ")
hlbka = input("Hĺbka bazéna (m): ")
okraj = input("Hĺbka hladiny od okraja (cm): ")
cena = input("Cena za m³ vody v €: ")

dlzka = float(dlzka)
sirka = float(sirka)
hlbka = float(hlbka)
okraj = int(okraj)
cena = float(cena)

V = dlzka * sirka * (hlbka - (okraj / 100))

print(f"Na bazén sa minie {V * 1000} litrov vody a bude to stáť {cena * V} €.")
