import tkinter
import math


w, h = 600, 600
canvas = tkinter.Canvas(width=w, height=h, bg="white")
canvas.pack()

x = w // 2
r = 30
alpha = 0
amp_max = h * 0.4

while amp_max > 1:
    y = int(amp_max * math.sin(alpha)) + (h // 2)
    canvas.create_line(x, y, x, 0)
    canvas.create_oval(x - r, y - r, x + r, y + r, fill="black")
    alpha += 0.1        # rychlost
    amp_max -= 0.5      # spomalovanie

    canvas.update()
    canvas.after(1000 // 30)
    canvas.delete("all")

y = (h // 2)
canvas.create_line(x, y, x, 0)
canvas.create_oval(x - r, y - r, x + r, y + r, fill="black")

canvas.mainloop()
