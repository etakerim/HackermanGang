# Write your code here :-)
def translate(x, a, b, m, n):
    y = (x - a) / (b - a)
    return m + (y * (n - m))