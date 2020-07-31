from pygame import *

CIERNA = Color(0, 0, 0)
BIELA = Color(255, 255, 255)

ZELENA = Color(0, 255, 0)
CERVENA = Color(255, 0, 0)
ORANZOVA = Color(255, 255, 0)

okno = display.set_mode([1200, 900])

X = 500
Y = 100
SIRKA = 400
VYSKA = int(SIRKA * 1.5)
POLOMER = SIRKA // 6

# Nakreslíme semafór
okno.fill(BIELA)
# Okraj
draw.rect(okno, CIERNA, Rect([X, Y], [SIRKA, VYSKA]), 1)
# Horné červené svetlo
draw.circle(okno, CERVENA, [X + SIRKA // 2, Y + SIRKA // 4], POLOMER)
# Stredné oranžové svetlo
draw.circle(okno, ORANZOVA, [X + SIRKA // 2, Y + SIRKA // 2 + SIRKA // 4], POLOMER)
# Dolné zelené svetlo
draw.circle(okno, ZELENA, [X + SIRKA // 2, Y + 2 * (SIRKA // 2) + SIRKA // 4], POLOMER)

while True:
    udalost = event.poll()
    if udalost.type == MOUSEBUTTONDOWN and udalost.button == 1:
        # Po stalčení ľavého tlačidla myši zistíme vzdialenosť od
        # horného červeného svetla
        vzX = udalost.pos[0] - (X + SIRKA // 2)     # Počet krokov po x-ovej osi
        vzY = udalost.pos[1] - (Y + SIRKA // 4)     # Počet krokov po y-ovej osi

        # Výpočet vzdialenosti medzi pozíciou pri klinkutí myši a stredom kruhu
        # Pytagorova veta: https://oskole.detiamy.sk/clanok/pytagorova-veta-a-jej-odvodenie
        vz = (vzX ** 2 + vzY ** 2) ** (1/2)

        if vz <= POLOMER:
            # Ak sa nachádza vnútri kruhu prefarbíme na semaforové svetlo na čiernu
            draw.circle(okno, CIERNA, [X + SIRKA // 2, Y + SIRKA // 4], POLOMER)
        else:
            # Ak sa nachádza mimo kruhu prefarbíme na semaforové svetlo späť na červenú
            draw.circle(okno, CERVENA, [X + SIRKA // 2, Y + SIRKA // 4], POLOMER)

    display.update()