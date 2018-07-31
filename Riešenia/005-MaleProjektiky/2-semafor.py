import tkinter

w, h = 600, 400
canvas = tkinter.Canvas(width=w, height=h, bg="white")
canvas.pack()

def semafor(x, y, h, s):
    d = h // 3
    k = d // 6
    colors = [{True: "#ff0000", False: "#500000"},
              {True: "#ffa000", False: "#835200"},
              {True: "#00ff00", False: "#005000"}]

    lights = [(x + 3*k, y + 3*k, 2*k, colors[0][s[0]]),
              (x + 3*k, y + 9*k, 2*k,  colors[1][s[1]]),
              (x + 3*k, y + 15*k, 2*k, colors[2][s[2]])]

    canvas.delete("all")
    canvas.create_rectangle(x, y, x + d, y + h, fill="black")

    for light in lights:
        canvas.create_oval(light[0] - light[2], light[1] - light[2],
                           light[0] + light[2], light[1] + light[2],
                           fill=light[3])
    return lights


def click(mouse):
    global lights, states
    x, y = mouse.x, mouse.y

    for i, s in enumerate(lights, start=0):
        if ((x - s[0]) ** 2 + (y - s[1]) ** 2) <= s[2] ** 2:
            states[i] = not states[i]
            lights = semafor(x=150, y=50, h=300, s=states)
            return


states = [True, False, False]
lights = semafor(x=150, y=50, h=300, s=states)

canvas.bind("<Button-1>", click)
canvas.mainloop()


"""
canvas.create_oval(x + k, y + k, x + 5 * k, y + 5 * k, fill="red")
canvas.create_oval(x + k, y + 7 * k, x + 5 * k, y + 11 * k, fill="orange")
canvas.create_oval(x + k, y + 13 * k, x + 5 * k, y + 17 * k, fill="green")
"""
