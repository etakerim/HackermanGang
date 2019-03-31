import tkinter


def vytvor_utvar(mys):
    global klik, utvar, mod, tlacidlo_vyber, farba

    if mys.x >= naradie_x:
        for m, btn in zip(nastroje, tlacidla):
            pos = okno.coords(btn)
            if (mys.x >= pos[0] and mys.x <= pos[2] and
                    mys.y >= pos[1] and mys.y <= pos[3]):
                mod = m
                okno.itemconfig(tlacidlo_vyber, fill='white')
                okno.itemconfig(btn, fill='#ccc')
                tlacidlo_vyber = btn

        f = vyber_farbu(mys.x, mys.y, naradie_x + naradie_w // 2, H - 80, 40)
        if f:
            rgb = (int(f[0] * 255), int(f[1] * 255), int(f[2] * 255))
            farba = '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])
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

    return [a, b, c]


def farebna_paleta(r):
    from math import sin, cos, radians
    from PIL import Image, ImageTk

    img = Image.new('HSV', (2 * r, 2 * r), color=(0, 0, 255))
    pixels = img.load()

    angle = 0
    while angle <= 360:             # hue
        for distance in range(r):   # saturation
            pos_x = r + distance * cos(radians(angle))
            pos_y = r + distance * sin(radians(angle))
            h = int(255 * (angle / 360))
            s = int(255 * (distance / r))
            pixels[pos_x, pos_y] = (h, s, 255)
        angle += 0.3

    return ImageTk.PhotoImage(image=img)


def vyber_farbu(mys_x, mys_y, x, y, r):
    from colorsys import hsv_to_rgb
    from math import hypot, atan2, degrees

    a0 = degrees(atan2(mys_y - y, mys_x - x))
    if a0 < 0:
        a0 += 360

    r0 = hypot(mys_x - x, mys_y - y)
    if r0 > r:
        return False
    else:
        return hsv_to_rgb(a0 / 360, r0 / r, 1)


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

img = farebna_paleta(40)
colorwheel = okno.create_image(naradie_x + naradie_w // 2, H - 80, image=img)

okno.mainloop()
