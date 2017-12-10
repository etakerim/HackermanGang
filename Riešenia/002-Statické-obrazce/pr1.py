import tkinter

x = 800
y = 600
platno = tkinter.Canvas(width=x, height=y, bg='white')
platno.pack()

# Diagonály
platno.create_line(0, 0, x, y, fill='red', width=3)
platno.create_line(0, y, x, 0, fill='red', width=3)

# Vertikálna a horizontálna čiara
platno.create_line(x // 2, 0, x // 2, y, width=3)
platno.create_line(0, y // 2, x, y // 2, width=3)

platno.mainloop()
