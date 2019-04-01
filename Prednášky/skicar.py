# http://effbot.org/tkinterbook/canvas.htm
# http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/canvas-methods.html

import tkinter
import math
import colorsys
from PIL import Image, ImageTk


def svg_ulozit():
    with open('drawing.svg', 'w') as svg:
        print('<?xml version="1.0" encoding="utf-8"?>', file=svg)
        print((f'<svg xmlns="http://www.w3.org/2000/svg" '
               f'width="{W - naradie_w}" height="{H}">'), file=svg)

        for tvar in okno.find_withtag('shape'):
            typ = okno.type(tvar)
            pos = [int(x) for x in okno.coords(tvar)]
            fill = None
            stroke = None

            if typ == 'line':
                wstroke = int(float(okno.itemcget(tvar, 'width')))
                print((f'\t<line x1="{pos[0]}" y1="{pos[1]}" '
                       f'x2="{pos[2]}" y2="{pos[3]}" '
                       f'stroke-width="{wstroke}"'),
                      file=svg, end='')
                stroke = okno.itemcget(tvar, 'fill')

            elif typ == 'rectangle':
                print((f'\t<rect x="{pos[0]}" y="{pos[1]}" '
                       f'width="{pos[2]}" height="{pos[3]}"'),
                      file=svg, end='')
                stroke = okno.itemcget(tvar, 'outline')
                fill = okno.itemcget(tvar, 'fill') or 'none'

            elif typ == 'oval':
                print(pos)
                rx = (pos[2] - pos[0]) // 2
                ry = (pos[3] - pos[1]) // 2
                cx = pos[0] + rx
                cy = pos[1] + ry
                print(cx, cy, rx, ry)
                print((f'\t<ellipse cx="{cx}" cy="{cy}" '
                       f'rx="{rx}" ry="{ry}"'), file=svg, end='')
                stroke = okno.itemcget(tvar, 'outline')
                fill = okno.itemcget(tvar, 'fill') or 'none'

            if stroke:
                print(f' stroke="{stroke}"', file=svg, end='')
            if fill:
                print(f' fill="{fill}"', file=svg, end='')
            print(f' />', file=svg)

        print('</svg>', file=svg)


def csv_ulozit():
    with open('drawing.csv', 'w') as svg:
        for tvar in okno.find_withtag('shape'):
            typ = okno.type(tvar)
            pos = [int(x) for x in okno.coords(tvar)]
            outline = ''
            if typ != 'line':
                outline = okno.itemcget(tvar, 'outline')
            fill = okno.itemcget(tvar, 'fill')
            print(typ, *pos, fill, outline, file=svg)


def csv_nacitat(nazov):
    with open(nazov, 'r') as svg:
        for cmd in svg:
            settings = cmd.split()
            if len(settings) >= 6:

                fill = None
                if len(settings) == 7:
                    fill = settings[6]
                outline = settings[5]

                pos = [int(x) for x in settings[1:5]]
                if settings[0] == 'line':
                    okno.create_line(*pos, fill=outline)
                elif settings[0] == 'rectangle':
                    okno.create_rectangle(*pos, outline=outline, fill=fill)
                elif settings[0] == 'oval':
                    okno.create_oval(*pos, outline=outline, fill=fill)


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
    global mod, tlacidlo_vyber, farba, vypln, color_preview

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

    if je_stlacene(uloz_btn, mys):
        svg_ulozit()
        # csv_ulozit()

    color = vyber_farbu(mys)
    if color:
        farba = '#{:02x}{:02x}{:02x}'.format(*color)
        okno.itemconfig(color_preview, fill=farba)
        if vypln:
            vypln = farba


def vytvor_utvar(mys):
    global klik, utvar

    klik = not klik
    if klik:
        if mod == CIARA:
            utvar = okno.create_line(mys.x, mys.y, mys.x, mys.y, fill=farba,
                                     tags='shape')
        elif mod == OBDLZNIK:
            utvar = okno.create_rectangle(mys.x, mys.y, mys.x, mys.y,
                                          outline=farba, fill=vypln,
                                          tags='shape')
        elif mod == ELIPSA:
            utvar = okno.create_oval(mys.x, mys.y, mys.x, mys.y,
                                     outline=farba, fill=vypln,
                                     tags='shape')
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
        if vypln:
            vypln = farba

    elif klavesa.char == 'v':
        if vypln:
            vypln = None
            okno.itemconfig(je_vypln, fill='white')
        else:
            vypln = farba
            okno.itemconfig(je_vypln, fill='black')


def zmaz_utvar(mys):
    predmet = okno.find_closest(mys.x, mys.y)
    tags = okno.gettags(predmet)
    if predmet and tags:
        if 'shape' in tags:
            okno.delete(predmet)


def panel_nastrojov():
    global color_preview, uloz_btn, je_vypln, uloz_btn

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

    color_preview = okno.create_rectangle(btn_xtop, 10 * btn_w,
                                          btn_xtop + btn_w, 11 * btn_w, fill=farba)
    pad = naradie_w // 8
    uloz_btn = okno.create_rectangle(naradie_x + pad, 8 * btn_w,
                                     W - pad, 9 * btn_w)
    okno.create_text(btn_xtop, int(8.5 * btn_w), text='Uložiť')

    btn_w = 20
    okno.create_text(naradie_x + pad + int(2.5 * btn_w), int(17.5 * btn_w), text='Výplň')
    je_vypln = okno.create_rectangle(naradie_x + pad, 17 * btn_w,
                                     naradie_x + pad + btn_w, 18 * btn_w)

    return [a, b, c]


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

svgfilename = input('Zadajte vstupný súbor alebo stlačte <Enter> pre nový: ')
okno = tkinter.Canvas(width=W, height=H, bg='white')
okno.pack()
okno.bind('<Button-1>', klik_mysou)
okno.bind('<Button-3>', zmaz_utvar)
okno.bind('<Motion>', animuj_utvar)
okno.bind_all('<Key>', zmen_utvar)

naradie_w = 100
naradie_x = W - naradie_w
btn_w = 30
color_preview = None
je_vypln = None
uloz_btn = None
tlacidla = panel_nastrojov()

tlacidlo_vyber = tlacidla[0]
okno.itemconfig(tlacidlo_vyber, fill='#ccc')

img = farebna_paleta(40)
colorwheel = okno.create_image(naradie_x + naradie_w // 2, H - 80, image=img)

if svgfilename:
    csv_nacitat(svgfilename)

okno.mainloop()
