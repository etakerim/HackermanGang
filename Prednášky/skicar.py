import tkinter


def vytvor_utvar(mys):
    global klik, utvar, mod, tlacidlo_vyber

    if mys.x >= naradie_x:
        for m, btn in zip(nastroje, tlacidla):
            pos = okno.coords(btn)
            if (mys.x >= pos[0] and mys.x <= pos[2] and
                    mys.y >= pos[1] and mys.y <= pos[3]):
                mod = m
                okno.itemconfig(tlacidlo_vyber, fill='white')
                okno.itemconfig(btn, fill='#ccc')
                tlacidlo_vyber = btn
        return

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

    if klavesa.char in nastroje:
        mod = klavesa.char

    elif klavesa.char in ['0', '1', '2', '3']:
        farba = paleta[int(klavesa.char)]

    elif klavesa.char == '@':
        if vypln:
            vypln = None
        else:
            vypln = farba


def panel_nastrojov():
    okno.create_line(naradie_x, 0, naradie_x, H, width=2)

    btn_w = int(0.3 * naradie_w)
    pad = int(0.25 * btn_w)
    btn_xtop = naradie_x + naradie_w // 2 - btn_w // 2

    a = okno.create_rectangle(btn_xtop, 2 * btn_w,
                              btn_xtop + btn_w, 3 * btn_w)
    okno.create_line(btn_xtop + pad, 2 * btn_w + pad,
                     btn_xtop + btn_w - pad, 3 * btn_w - pad, width=2)
    b = okno.create_rectangle(btn_xtop, 4 * btn_w,
                              btn_xtop + btn_w, 5 * btn_w)
    okno.create_rectangle(btn_xtop + pad, 4 * btn_w + pad,
                          btn_xtop + btn_w - pad, 5 * btn_w - pad, fill='black')
    c = okno.create_rectangle(btn_xtop, 6 * btn_w, btn_xtop + btn_w, 7 * btn_w)
    okno.create_oval(btn_xtop + pad, 6 * btn_w + pad,
                     btn_xtop + btn_w - pad, 7 * btn_w - pad, fill='black')
    colorwheel(300, 200, 80)

    return [a, b, c]


def colorwheel(x, y, radius):
    from colorsys import hsv_to_rgb
    from math import sin, cos, radians

    for angle in range(360):            # hue
        for distance in range(radius):  # saturation
            pos_x = x + distance * cos(radians(angle))
            pos_y = y - distance * sin(radians(angle))
            r, g, b = hsv_to_rgb(angle / 360, distance / radius, 1)
            c = '#{:02x}{:02x}{:02x}'.format(int(r * 255), int(g * 255), int(b * 255))
            okno.create_rectangle(pos_x, pos_y, pos_x+1, pos_y+1, fill=c, outline=c)


W, H = 800, 500
klik = False
utvar = None

CIARA = 'c'
OBDLZNIK = 'o'
ELIPSA = 'e'
mod = CIARA
nastroje = [CIARA, OBDLZNIK, ELIPSA]

paleta = ['black', 'red', 'green', 'blue']
farba = paleta[0]
vypln = None

okno = tkinter.Canvas(width=W, height=H, bg='white')
okno.pack()
okno.bind('<Button-1>', vytvor_utvar)
okno.bind('<Motion>', animuj_utvar)
okno.bind_all("<Key>", zmen_utvar)

naradie_w = 100
naradie_x = W - naradie_w
tlacidla = panel_nastrojov()

tlacidlo_vyber = tlacidla[0]
okno.itemconfig(tlacidlo_vyber, fill='#ccc')

okno.mainloop()
