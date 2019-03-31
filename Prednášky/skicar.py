import tkinter


def vytvor_utvar(mys):
    global klik, utvar

    klik = not klik
    if klik:
        utvar = okno.create_line(mys.x, mys.y, mys.x, mys.y)
    else:
        pos = okno.coords(utvar)
        okno.coords(utvar, pos[0], pos[1], mys.x, mys.y)


W, H = 800, 500
klik = False
utvar = 0

okno = tkinter.Canvas(width=W, height=H, bg='white')
okno.pack()
okno.bind('<Button-1>', vytvor_utvar)
okno.mainloop()
