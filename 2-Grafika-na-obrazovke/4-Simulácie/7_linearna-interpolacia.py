from pygame import *

A = [100, 100]
B = [500, 300]
r = 10

canvas = display.set_mode((600, 400))
x, y = A

# return (1 - t) * a + t * b
def lerp(a, b, t):
    c = a + t * (b - a)
    return int(c)

c = 0
while True:
    canvas.fill(Color(0, 0, 0))

    draw.circle(canvas, Color(128, 0, 128), A, r)
    draw.circle(canvas, Color(128, 0, 128), B, r)
    draw.line(canvas, Color(255, 255, 255), A, B)

    x = lerp(A[0], B[0], c)
    y = lerp(A[1], B[1], c)
    draw.circle(canvas, Color(0, 230, 0), [x, y], r)

    c += 0.02
    if c > 1:
        c = 1

    display.update()
    time.delay(30)