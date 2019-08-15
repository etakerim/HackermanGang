from datetime import datetime
from datetime import timedelta

csv_nazov = input("Prečítaj narodeniny zo súboru (.csv): ")
ics_nazov = input("Priprav kalendár s názvom (.ics): ")

narodeniny = open(csv_nazov, "r")
kalendar = open(ics_nazov, "w")
ciselnik = 0

print("BEGIN:VCALENDAR", file=kalendar)
print("PRODID:Programatorsky kruzok", file=kalendar)
print("VERSION:2.0", file=kalendar)

for osoba in narodeniny:
    osoba = osoba.split(",")
    meno = osoba[0].strip()
    narodenie = osoba[1].strip()

    print("BEGIN:VEVENT", file=kalendar)

    # Pre zjednodušenie prečítaj časovú značku na vstupe.
    casova_znacka = datetime.now().strftime("%Y%m%dT%H%M%SZ")
    print(f"DTSTAMP:{casova_znacka}", file=kalendar)

    # Podľa správnosti by si mal vygenerovať jedinečný kód, napríklad takto:
    # from uuid import uuid1
    # ciselnik = uuid1()
    ciselnik += 1
    print(f"UID:{ciselnik}", file=kalendar)

    # Krátky popis a kategória udalosti v kalendári. Ide o narodeniny.
    print(f"SUMMARY:{meno} narodeniny", file=kalendar)
    print("CATEGORIES:Narodeniny", file=kalendar)

    # Kalendár zobrazí udalosť každý rok
    print("RRULE:FREQ=YEARLY", file=kalendar)

    # Pre zjednodušenie zostav dátum narodenín spájaním reťazcov.
    datum = datetime.strptime(narodenie, "%d.%m.%Y")
    start = datum.strftime("%Y%m%d")
    print(f"DTSTART;VALUE=DATE:{start}", file=kalendar)

    koniec = datum + timedelta(days=1)
    koniec = koniec.strftime("%Y%m%d")
    print(f"DTEND;VALUE=DATE:{koniec}", file=kalendar)

    # Umožní vytvárať aj iné udalosti na deň narodenín
    print("TRANSP:TRANSPARENT", file=kalendar)

    # Pripomienka týždeň pred narodeninami
    print("BEGIN:VALARM", file=kalendar)
    print("DESCRIPTION:", file=kalendar)
    print("ACTION:DISPLAY", file=kalendar)
    print("TRIGGER:-P7D", file=kalendar)
    print("END:VALARM", file=kalendar)

    print("END:VEVENT", file=kalendar)

print("END:VCALENDAR", file=kalendar)
print("Hotovo.")

narodeniny.close()
kalendar.close()
