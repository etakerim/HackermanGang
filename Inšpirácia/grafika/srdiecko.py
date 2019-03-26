from PIL import Image, ImageDraw
from math import pi, sin, cos

image = Image.new('RGB', (950, 900), (255, 255, 255))
draw = ImageDraw.Draw(image)

t = 0
points = []
s = 25

while t <= 2 * pi:
    x = 16 * (sin(t)) ** 3
    y = 13 * cos(t) - 5 * cos(2*t) - 2 * cos(3*t) - cos(4*t)
    points.append((s * x + image.width // 2, -s * y + image.height // 2))
    t += 0.001

draw.polygon(points, fill=(255, 0, 0))
image.save('srdce.png')
