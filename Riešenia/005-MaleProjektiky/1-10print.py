import tkinter
import random

w, h = 600, 400
canvas = tkinter.Canvas(width=w, height=h, bg="white")
canvas.pack()

n = 10      # Change resolution - num of columns and rows
a = w // n

for y in range(0, h, a):
    for x in range(0, w, a):
        if random.random() > 0.5:
            canvas.create_line(x, y, x + a, y + a)
        else:
            canvas.create_line(x + a, y, x, y + a)

canvas.mainloop()
