import tkinter


def vytvor_utvar(mys):
    global klik, utvar

    klik = not klik
    if klik:
        if mod == CIARA:
            utvar = okno.create_line(mys.x, mys.y, mys.x, mys.y)
        elif mod == OBDLZNIK:
            utvar = okno.create_rectangle(mys.x, mys.y, mys.x, mys.y)
        elif mod == ELIPSA:
            utvar = okno.create_oval(mys.x, mys.y, mys.x, mys.y)
    else:
        pos = okno.coords(utvar)
        okno.coords(utvar, pos[0], pos[1], mys.x, mys.y)


def animuj_utvar(mys):
    if klik:
        pos = okno.coords(utvar)
        okno.coords(utvar, pos[0], pos[1], mys.x, mys.y)


def zmen_utvar(klavesa):
    global mod

    if klavesa.char in [CIARA, OBDLZNIK, ELIPSA]:
        mod = klavesa.char


W, H = 800, 500
klik = False
utvar = 0

CIARA = 'c'
OBDLZNIK = 'o'
ELIPSA = 'e'
mod = CIARA

okno = tkinter.Canvas(width=W, height=H, bg='white')
okno.pack()
okno.bind('<Button-1>', vytvor_utvar)
okno.bind('<Motion>', animuj_utvar)
okno.bind_all("<Key>", zmen_utvar)
okno.mainloop()
