from pygame import *

def edges_of(vertices):
    edges = []

    N = len(vertices)
    for i in range(N):
        e = vertices[(i + 1) % N] - vertices[i]
        edges.append(e)

    return edges


def orthogonal(v):
    return Vector2(-v.y, v.x)

def is_separating_axis(axis, p1, p2):
    min_p1 = float("inf")
    max_p1 = float("-inf")
    for p in p1:
        projection = p.dot(axis)
        min_p1 = min(min_p1, projection)
        max_p1 = max(max_p1, projection)

    min_p2 = float("inf")
    max_p2 = float("-inf")
    for p in p2:
        projection = p.dot(axis)
        min_p2 = min(min_p2, projection)
        max_p2 = max(max_p2, projection)

    if max_p1 >= min_p2 and max_p2 >= min_p1:
        return False
    else:
        return True


def polygon_collision(P1, P2):
    edges = edges_of(P1) + edges_of(P2)
    orthogonals = []
    for e in edges:
        orthogonals.append(orthogonal(e))

    for axis in orthogonals:
        if is_separating_axis(axis, P1, P2):
            return False
    return True


if __name__ == "__main__":
    screen = display.set_mode([600, 400])

    pos_5gon = Vector2(100, 100)
    pos_3gon = Vector2(300, 250)
    step = 5

    while True:
        screen.fill(Color(0, 0, 0))
        event.poll()
        k = key.get_pressed()

        if k[K_UP]:
            pos_5gon.y -= step
        elif k[K_DOWN]:
            pos_5gon.y += step
        elif k[K_RIGHT]:
            pos_5gon.x += step
        elif k[K_LEFT]:
            pos_5gon.x -= step

        if k[K_w]:
            pos_3gon.y -= step
        elif k[K_s]:
            pos_3gon.y += step
        elif k[K_d]:
            pos_3gon.x += step
        elif k[K_a]:
            pos_3gon.x -= step

        pentagon = []
        v = Vector2(50, 0)
        for i in range(5):
            pentagon.append(v + pos_5gon)
            v = v.rotate(360 // 5)

        triangle = []
        v = Vector2(20, 0)
        for i in range(3):
            triangle.append(v + pos_3gon)
            v = v.rotate(360 // 3)

        color = Color(255, 255, 255)
        if polygon_collision(pentagon, triangle):
            color = Color(255, 0, 0)

        draw.polygon(screen, color, [[int(v.x), int(v.y)] for v in pentagon], 1)
        draw.polygon(screen, color, [[int(v.x), int(v.y)] for v in triangle], 1)

        display.update()
        time.delay(20)


