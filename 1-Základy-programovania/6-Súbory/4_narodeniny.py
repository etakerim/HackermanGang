datum = input("Zobraz narodeniny pre mesiac v roku: ")
datum = datum.split(".")

NAZVY_MESIACOV = ["Január", "Február", "Marec", "Apríl", "Máj", "Jún", "Júl",
                  "August", "September", "Október", "November", "December"]
mesiac = int(datum[0])
rok = int(datum[1])

narodeniny = open("narodeniny.csv", "r")
print(f"\nNarodeniny: {NAZVY_MESIACOV[mesiac - 1]} {rok}")

for osoba in narodeniny:
    osoba = osoba.split(",")
    meno = osoba[0]
    datum = osoba[1].split(".")

    narodenie_den = int(datum[0])
    narodenie_mesiac = int(datum[1])
    narodenie_rok = int(datum[2])

    if narodenie_mesiac == mesiac:
        print(f"{narodenie_den}.{narodenie_mesiac} - {meno} - "
              f"{rok - narodenie_rok} rokov")

narodeniny.close()
