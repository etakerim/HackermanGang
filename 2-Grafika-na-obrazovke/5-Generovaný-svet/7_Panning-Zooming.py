from pygame import *

WIDTH = 1280
HEIGHT = 800
screen = display.set_mode([WIDTH, HEIGHT])

BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
RED = Color(255, 0, 0)

OffsetX = -WIDTH / 2
OffsetY = -HEIGHT / 2

StartPanX = 0
StartPaxY = 0

ScaleX = 1
ScaleY = 1

held = False

selectCellX = 0
selectCellY = 0

def WorldToScreen(WorldX, WorldY):
    return int((WorldX - OffsetX) * ScaleX), int((WorldY - OffsetY) * ScaleY)

def ScreenToWorld(ScreenX, ScreenY):
    return (ScreenX / ScaleX + OffsetX), (ScreenY / ScaleX + OffsetY)

while True:
    for ev in event.get():
        if ev.type == MOUSEBUTTONDOWN:
            if ev.button == 1:
                held = True
                StartPanX, StartPanY = ev.pos
            elif ev.button == 3:
                selectCellX, selectCellY = map(int, ScreenToWorld(*ev.pos))
            elif ev.button == 4 or ev.button == 5:
                mxWorld, myWorld = ScreenToWorld(*ev.pos)
                if ev.button == 4:
                    ScaleX *= 1.05
                    ScaleY *= 1.05
                elif ev.button == 5:
                    ScaleX *= 0.95
                    ScaleY *= 0.95
                mxWorldAfter, myWorldAfter = ScreenToWorld(*ev.pos)
                OffsetX += (mxWorld - mxWorldAfter)
                OffsetY += (myWorld - myWorldAfter)
        elif ev.type == MOUSEBUTTONUP and ev.button == 1:
            held = False
        elif ev.type == MOUSEMOTION and held:
            mx, my = ev.pos
            OffsetX -= (mx - StartPanX)
            OffsetY -= (my - StartPanY)
            StartPanX = mx
            StartPanY = my
        elif ev.type == QUIT:
            quit()

    # Draw ---------
    screen.fill(BLACK)
    # Clip Screen
    worldLeft, worldTop = ScreenToWorld(0, 0)
    worldRight, worldBottom = ScreenToWorld(WIDTH, HEIGHT)

    for y in range(11):
        if worldTop <= y <= worldBottom:
            draw.line(screen, WHITE, WorldToScreen(0, y), WorldToScreen(10, y))
    for x in range(11):
        if worldLeft <= x <= worldRight:
            draw.line(screen, WHITE, WorldToScreen(x, 0), WorldToScreen(x, 10))

    draw.circle(screen, RED, WorldToScreen(selectCellX + 0.5, selectCellY + 0.5), int(0.3 * ScaleX))

    display.update()
    time.delay(30)