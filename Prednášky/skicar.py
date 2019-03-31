import tkinter


def vytvor_utvar(mys):
    global klik, utvar

    klik = not klik
    if klik:
        if mod == CIARA:
            utvar = okno.create_line(mys.x, mys.y, mys.x, mys.y, fill=farba)
        elif mod == OBDLZNIK:
            utvar = okno.create_rectangle(mys.x, mys.y, mys.x, mys.y,
                                          outline=farba, fill=vypln)
        elif mod == ELIPSA:
            utvar = okno.create_oval(mys.x, mys.y, mys.x, mys.y,
                                     outline=farba, fill=vypln)
    else:
        pos = okno.coords(utvar)
        okno.coords(utvar, pos[0], pos[1], mys.x, mys.y)


def animuj_utvar(mys):
    if klik:
        pos = okno.coords(utvar)
        okno.coords(utvar, pos[0], pos[1], mys.x, mys.y)


def zmen_utvar(klavesa):
    global mod, farba, vypln

    if klavesa.char in [CIARA, OBDLZNIK, ELIPSA]:
        mod = klavesa.char

    elif klavesa.char in ['0', '1', '2', '3']:
        farba = paleta[int(klavesa.char)]

    elif klavesa.char == '@':
        if vypln:
            vypln = None
        else:
            vypln = farba


W, H = 800, 500
klik = False
utvar = None

CIARA = 'c'
OBDLZNIK = 'o'
ELIPSA = 'e'
mod = CIARA

paleta = ['black', 'red', 'green', 'blue']
farba = paleta[0]
vypln = None

okno = tkinter.Canvas(width=W, height=H, bg='white')
okno.pack()
okno.bind('<Button-1>', vytvor_utvar)
okno.bind('<Motion>', animuj_utvar)
okno.bind_all("<Key>", zmen_utvar)
okno.mainloop()
