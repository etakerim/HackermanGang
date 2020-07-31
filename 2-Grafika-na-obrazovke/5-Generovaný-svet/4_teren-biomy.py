from pygame import *
from random import *
from opensimplex import *

WIDTH = 600
HEIGHT = 400
screen = display.set_mode([WIDTH, HEIGHT])

altitude = OpenSimplex(randrange(1000))
moisture = OpenSimplex(randrange(1000))
zoom = 6

def noise1(nx, ny):
    return altitude.noise2d(zoom * nx, zoom * ny) / 2 + 0.5

def noise2(nx, ny):
    return moisture.noise2d(zoom * nx, zoom * ny) / 2 + 0.5

def biome(elevation, moisture):
    OCEAN = Color(67, 67, 122)
    BEACH = Color(147, 134, 119)
    SNOW = Color(222, 222, 229)
    TUNDRA = Color(188, 188, 171)
    BARE = Color(136, 136, 136)
    SCORCHED = Color(85, 85, 85)
    TAIGA = Color(153, 171, 119)
    SHRUBLAND= Color(136, 153, 119)
    TEMPERATE_DESERT = Color(201, 210, 155)
    TEMPERATE_RAIN_FOREST = Color(67, 136, 85)
    TEMPERATE_DECIDUOUS_FOREST = Color(103, 147, 89)
    GRASSLAND = Color(136, 171, 85)
    SUBTROPICAL_DESERT = Color(210, 185, 139)
    TROPICAL_RAIN_FOREST = Color(51, 119, 85)
    TROPICAL_SEASONAL_FOREST = Color(86, 153, 68)

    if elevation < 0.1:
        return OCEAN
    elif elevation < 0.12:
        return BEACH
    elif elevation < 0.3:
        if moisture < 0.16:
            return SUBTROPICAL_DESERT
        elif moisture < 0.33:
            return GRASSLAND
        elif moisture < 0.66:
            return TROPICAL_SEASONAL_FOREST
        else:
            return TROPICAL_RAIN_FOREST
    elif elevation < 0.6:
        if moisture < 0.16:
            return TEMPERATE_DESERT
        elif moisture < 0.50:
            return GRASSLAND
        elif moisture < 0.83:
            return TEMPERATE_DECIDUOUS_FOREST
        else:
            return TEMPERATE_RAIN_FOREST
    elif elevation < 0.8:
        if moisture < 0.33:
            return TEMPERATE_DESERT
        elif moisture < 0.66:
            return SHRUBLAND
        else:
            return TAIGA
    else:
        if moisture < 0.1:
            return SCORCHED
        elif moisture < 0.2:
            return BARE
        elif moisture < 0.5:
            return TUNDRA
        else:
            return SNOW

biomes = image.load("biome-lookup-discrete.png")

def biome_lookup(elevation, moisture):
    x = int(moisture * biomes.get_width())
    y = int((1 - elevation) * biomes.get_height())
    return biomes.get_at([x, y])

for y in range(HEIGHT):
    for x in range(WIDTH):
        nx = x / WIDTH - 0.5
        ny = y / HEIGHT - 0.5

        e =   (1.00 * noise1(1 * nx, 1 * ny)
             + 0.50 * noise1(2 * nx, 2 * ny)
             + 0.25 * noise1(4 * nx, 4 * ny)
             + 0.13 * noise1(8 * nx, 8 * ny)
             + 0.06 * noise1(16 * nx, 16 * ny)
             + 0.03 * noise1(32 * nx, 32 * ny))
        e /= (1.00 + 0.50 + 0.25 + 0.13 + 0.06 + 0.03)
        e = e ** 2.4

        m =   (0.74 * noise2(1 * nx, 1 * ny)
             + 0.54 * noise2(2 * nx, 2 * ny)
             + 0.33 * noise2(4 * nx, 4 * ny)
             + 0.33 * noise2(8 * nx, 8 * ny)
             + 0.33 * noise2(16 * nx, 16 * ny)
             + 0.50 * noise2(32 * nx, 32 * ny))
        m /= (0.74 + 0.54 + 0.33 + 0.33 + 0.33 + 0.50)

        # screen.set_at([x, y], biome(e, m))
        screen.set_at([x, y], biome_lookup(e, m))

while True:
    display.update()
    time.delay(30)