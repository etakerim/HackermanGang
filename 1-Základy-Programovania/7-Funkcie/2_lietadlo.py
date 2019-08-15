from math import sin, cos, acos, radians


def letime(x, y):
    POLOMER_ZEME = 6371.11
    uhol = acos(sin(x[0]) * sin(y[0]) +
                cos(x[0]) * cos(y[0]) * cos(abs(x[1] - y[1])))
    obluk = POLOMER_ZEME * uhol
    return obluk


start = input("Pozícia: ")
ciel = input("Cieľ: ")

start = start.split(" ")
start = [
    radians(float(start[0])),
    radians(float(start[1]))
]
ciel = ciel.split(" ")
ciel = [
    radians(float(ciel[0])),
    radians(float(ciel[1]))
]

vzdielenost = letime(start, ciel)
print(f"\nVzdialenosť: {vzdielenost:.2f} km")
