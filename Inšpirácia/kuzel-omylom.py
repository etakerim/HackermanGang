from tkinter import *

platno = Canvas(width=600, height=500, bg='white')
platno.pack()

x = 0
y = 500 // 2
r = 20

while True:
    # platno.create_oval(x - r, y - r, x + r, y + r, fill='red')
    platno.create_oval(x - r, x + r, y - r, y + r, fill='red')
    x += 5
    platno.update()
    platno.after(1)
    # platno.delete(ALL)
