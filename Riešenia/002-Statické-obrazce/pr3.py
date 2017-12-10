import tkinter
import random

n = 250
spc = 20

sirka = 800
vyska = 600
platno = tkinter.Canvas(width=sirka, height=vyska, bg='white')
platno.pack()

# Čiary na zvýraznenie predelu
# platno.create_line(sirka // 2 - spc, 0, sirka // 2 - spc, vyska)
# platno.create_line(sirka // 2 + spc, 0, sirka // 2 + spc, vyska)

for i in range(n):
    # Vyber náhodné súradnice a polomer
    x = random.randint(0, sirka)
    y = random.randint(0, vyska)
    r = random.randint(10, 40)

    # Ak je krúžok v predeli posuň k bližšej strane
    if x >= (sirka // 2) and x <= (sirka // 2 + spc + r):
        x += r + spc
    elif x >= (sirka // 2 - spc - r) and x <= (sirka // 2):
        x -= r + spc

    # Ofarbi na základe získanej pozície
    if x > sirka // 2:
        farba = 'blue'
    else:
        farba = 'green'


    platno.create_oval(x - r, y - r, x + r, y + r, fill=farba)

platno.mainloop()
