import tkinter

x = 800
y = 600
platno = tkinter.Canvas(width=x, height=y, bg='white')
platno.pack()

x_kruh = x // 2
y_kruh = y // 2
r = 200

platno.create_oval(x_kruh - r, y_kruh - r, x_kruh + r, y_kruh + r)
platno.create_line(x_kruh, y_kruh - r,
                   x_kruh + r, y_kruh,
                   x_kruh - r, y_kruh,
                   x_kruh, y_kruh - r)

platno.mainloop()
