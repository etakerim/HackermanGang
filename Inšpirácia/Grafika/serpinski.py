from PIL import Image, ImageDraw

xk = 0.5
yk = 0.866025403
color = (255, 255, 255)
RX = 1000
RY = int(RX * yk)

def midsegments(x, y, a):
    if a < 1:
        return
    else:
        canvas.polygon([(x, y), (x + a, y), (x + xk * a, y + yk * a)],
                        outline=color)
        midsegments(x + xk * a * 0.5, y - yk * a * 0.5, a / 2)
        midsegments(x - xk * a * 0.5, y + yk * a * 0.5, a / 2)
        midsegments(x + a - xk * a * 0.5, y + yk * a * 0.5, a / 2)

def serpinski(x, y, a):
    canvas.polygon([(x, y), (x + a, y), (x + xk * a, y - yk * a)],
                outline=color)
    midsegments(x + xk * a * 0.5, y - yk * a * 0.5, a / 2)

img = Image.new('RGB', (RX, RY))
canvas = ImageDraw.Draw(img)
serpinski(x=img.width // 10, y=img.height - img.height // 10,
          a=8* (img.width // 10))

img.save('serpinski.png')
