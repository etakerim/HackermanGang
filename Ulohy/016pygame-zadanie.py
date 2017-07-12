# http://pygame.org/docs/
import pygame
from pygame.locals import *
import sys

# Konštanty
FPS = 60
OKNO_SIRKA = 640
OKNO_VYSKA = 480
FIELD_X    = 30
FIELD_Y    = 30
BARWIDTH   = 2
BCG_COLOR  = (0x05, 0xa4, 0xff)  # Svetlo modrá
GRID_COLOR = (0x7e, 0x3f, 0x11)  # Hnedá - vysvetliť hex získanie
OBJ_COLOR  = (0xff, 0xf0, 0x52)  # Bledo - žltá

def board2list(x, y):
    return ((x + BARWIDTH) // (OKNO_SIRKA // FIELD_X),
            (y + BARWIDTH) // (OKNO_VYSKA // FIELD_Y))

def list2board(row, col):
    x1 = row * (OKNO_SIRKA // FIELD_X) + BARWIDTH
    y1 = col * (OKNO_VYSKA // FIELD_Y) + BARWIDTH
    xdiff = ((row + 1) * (OKNO_SIRKA // FIELD_X)) - x1
    ydiff = ((col + 1) * (OKNO_VYSKA // FIELD_Y)) - y1
    return pygame.Rect(x1, y1, xdiff, ydiff)


def draw_board(surf, board):
    for x in range(0, OKNO_SIRKA, OKNO_SIRKA // FIELD_X):
        pygame.draw.line(surf, GRID_COLOR, (x, 0), (x, OKNO_VYSKA), BARWIDTH)

    for y in range(0, OKNO_SIRKA, OKNO_VYSKA // FIELD_Y):
        pygame.draw.line(surf, GRID_COLOR, (0, y), (OKNO_SIRKA, y), BARWIDTH)

    for i in range(FIELD_X):
        for j in range(FIELD_Y):
            if(board[i][j]):
                #print("{}, {}".format(i, j))
                pygame.draw.rect(surf, OBJ_COLOR, list2board(i, j))


def empty_board():
    board = []
    for i in range(FIELD_X):
        board.append([])
        for j in range(FIELD_Y):
            board[i].append(False)
    return board

def shift_up(board):
    newboard = empty_board()
    for i in range(0, FIELD_X):
        for j in range(1, FIELD_Y):
            newboard[i][j - 1] = gameboard[i][j]
    return newboard

def shift_down(board):
    newboard = empty_board()
    for i in range(0, FIELD_X):
        for j in range(0, FIELD_Y - 1):
            newboard[i][j + 1] = gameboard[i][j]
    return newboard

def shift_left(board):
    newboard = empty_board()
    for i in range(1, FIELD_X):
        newboard[i - 1] = gameboard[i]
    return newboard

def shift_right(board):
    newboard = empty_board()
    for i in range(0, FIELD_X - 1):
        newboard[i + 1] = gameboard[i]
    return newboard


# Inicializácia
pygame.init()
okno = pygame.display.set_mode((OKNO_SIRKA, OKNO_VYSKA))
pygame.display.set_caption("Grafický pokus")
casovac = pygame.time.Clock()

gameboard = empty_board()

# Hlavná herná slučka
while True:
    okno.fill(BCG_COLOR)
    draw_board(okno, gameboard)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == MOUSEBUTTONDOWN:
            # Pridaj do 2D zoznamu - ukáž kondenzovaný spôsob (krása Pythonu)
            mousex, mousey = event.pos
            i, j = board2list(mousex, mousey)
            gameboard[i][j] = not gameboard[i][j]  # Spôsob vymazania

        elif event.type == KEYDOWN:
            #Posuň položky v 2D zozname
            if event.key == K_UP:
                gameboard = shift_up(gameboard)
            elif event.key == K_DOWN:
                gameboard = shift_down(gameboard)
            elif event.key == K_RIGHT:
                gameboard = shift_right(gameboard)
            elif event.key == K_LEFT:
                gameboard = shift_left(gameboard)

    pygame.display.update()
    casovac.tick(FPS)
