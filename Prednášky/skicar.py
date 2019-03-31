import tkinter
import math
import colorsys
from PIL import Image, ImageTk


def klik_mysou(mys):
    if mys.x >= naradie_x:
        vyber_nastroj(mys)
    else:
        vytvor_utvar(mys)


def je_stlacene(tlacidlo, mys):
    pos = okno.coords(tlacidlo)
    return (mys.x >= pos[0] and mys.x <= pos[2] and
            mys.y >= pos[1] and mys.y <= pos[3])


def vyber_nastroj(mys):
    global mod, tlacidlo_vyber, farba, vypln

    for m, btn in zip(nastroje, tlacidla):
        if je_stlacene(btn, mys):
            mod = m
            okno.itemconfig(tlacidlo_vyber, fill='white')
            okno.itemconfig(btn, fill='#ccc')
            tlacidlo_vyber = btn

    if je_stlacene(je_vypln, mys):
        if vypln:
            vypln = None
            okno.itemconfig(je_vypln, fill='white')
        else:
            vypln = farba
            okno.itemconfig(je_vypln, fill='black')

    color = vyber_farbu(mys)
    if color:
        farba = '#{:02x}{:02x}{:02x}'.format(*color)
        if vypln:
            vypln = farba


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
    global mod, farba, vypln, je_vypln

    if klavesa.char in nastroje:
        mod = klavesa.char

    elif klavesa.char in ['0', '1', '2', '3']:
        farba = paleta[int(klavesa.char)]

    elif klavesa.char == 'v':
        if vypln:
            vypln = None
            okno.itemconfig(je_vypln, fill='white')
        else:
            vypln = farba
            okno.itemconfig(je_vypln, fill='black')


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


def tlacidlo_vyplne():
    btn_w = 20
    pad = naradie_w // 8
    okno.create_text(naradie_x + pad + int(2.5 * btn_w),
                     int(12.5 * btn_w), text='Výplň')
    return okno.create_rectangle(naradie_x + pad, 12 * btn_w,
                                 naradie_x + pad + btn_w, 13 * btn_w)


def farebna_paleta(r):
    img = Image.new('HSV', (2 * r, 2 * r), color=(0, 0, 255))
    pixels = img.load()

    angle = 0
    while angle <= 360:             # hue
        for distance in range(r):   # saturation
            a = math.radians(angle)
            pos_x = r + distance * math.cos(a)
            pos_y = r + distance * math.sin(a)
            h = int(255 * (angle / 360))
            s = int(255 * (distance / r))
            pixels[pos_x, pos_y] = (h, s, 255)
        angle += 0.3

    return ImageTk.PhotoImage(image=img)


def vyber_farbu(mys):
    pos = okno.bbox(colorwheel)
    r = (pos[2] - pos[0]) // 2
    x = pos[0] + r
    y = pos[1] + r

    a0 = math.degrees(math.atan2(mys.y - y, mys.x - x))
    if a0 < 0:
        a0 += 360

    r0 = math.hypot(mys.x - x, mys.y - y)
    if r0 > r:
        return False
    else:
        rgb = colorsys.hsv_to_rgb(a0 / 360, r0 / r, 1)
        return (int(rgb[0] * 255), int(rgb[1] * 255), int(rgb[2] * 255))


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
okno.bind('<Button-1>', klik_mysou)
okno.bind('<Motion>', animuj_utvar)
okno.bind_all("<Key>", zmen_utvar)

naradie_w = 100
naradie_x = W - naradie_w
tlacidla = panel_nastrojov()
je_vypln = tlacidlo_vyplne()

tlacidlo_vyber = tlacidla[0]
okno.itemconfig(tlacidlo_vyber, fill='#ccc')

img = farebna_paleta(40)
colorwheel = okno.create_image(naradie_x + naradie_w // 2, H - 80, image=img)

okno.mainloop()
