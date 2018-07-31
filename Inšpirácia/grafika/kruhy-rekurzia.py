from tkinter import *

def kruh(x, y, r):
    c.create_oval(x - r, y - r, x + r, y + r, outline="white")

def kruznice(x, y, r):
    if r < 5:
        return
    else:
        kruznice(x, y, r - 20)
 #       kruznice(x + r, y, r // 2)
 #       kruznice(x, y - r, r // 2)
 #       kruznice(x, y + r, r // 2)
        kruh(x, y, r)

c = Canvas(width=1200, height=600, bg="black")
c.pack()
kruznice(500, 300, 300)

c.mainloop()
