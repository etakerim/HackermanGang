import math

xsrc, ysrc = map(float, input("Štart (x, y): ").split(","))
xdst, ydst = map(float, input("Cieľ (x, y): ").split(","))

xdelta = xdst - xsrc
ydelta = ydst - ysrc

# math.sqrt(xdelta ** 2 + ydelta ** 2)
# https://cs.wikipedia.org/wiki/Arctg2

vzdialenost = math.hypot(xdelta, ydelta)
azimut = math.degrees(math.atan2(ydelta, xdelta))

print("Vzdialenosť je {:.2f} bodov a Azimut je {:.2f}°".format(vzdialenost, azimut))



