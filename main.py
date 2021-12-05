import pygame as pg
import sys
import numpy as np


"""Global variables"""
player = 1
game_over = False
xcolor = (158, 158, 158)
ocolor = (239, 231, 200)
cr = 60
cw = 15
kw = 25
space = 55

"""Board"""
board = np.zeros((3, 3))

"""Screen"""
width = 600
height = 600
screen = pg.display.set_mode((width, height))


def draw():

    """Variables"""
    pg.display.set_caption("TIC TAC TOE")
    line_color = (23, 135, 145)
    line_width = 15

    """BACKGROUND COLOR"""
    bg_color = (20, 170, 156)
    screen.fill(bg_color)

    """DRAW lINES"""
    pg.draw.line(screen, line_color, (0, 200), (600, 200), line_width)
    pg.draw.line(screen, line_color, (0, 400), (600, 400), line_width)
    pg.draw.line(screen, line_color, (200, 0), (200, 600), line_width)
    pg.draw.line(screen, line_color, (400, 0), (400, 600), line_width)


def mark_square(row, col, pl):
    """Board"""
    board[row][col] = pl


def available_square(row, col):
    return board[row][col] == 0


def is_board_full():
    for row in range(3):
        for col in range(3):
            if board[row][col] == 0:
                return False
    return True


def draw_vert_win_line(col, player):
    if player == 1:
        color = xcolor
    else:
        color = ocolor

    posx = col * 200 + 100

    pg.draw.line(screen, color, (posx, 15), (posx, height-15), 15)


def draw_hor_win_line(row, player):
    if player == 1:
        color = xcolor
    else:
        color = ocolor

    posy = row * 200 + 100

    pg.draw.line(screen, color, (15, posy), (width - 15, posy), 15)


def draw_asc_win_line(player):
    if player == 1:
        color = xcolor
    else:
        color = ocolor

    pg.draw.line(screen, color, (15, height - 15), (width - 15, 15), 15)


def draw_desc_win_line(player):
    if player == 1:
        color = xcolor
    else:
        color = ocolor

    pg.draw.line(screen, color, (15, 15), (width - 15, height - 15), 15)


def check_win(player):

    for col in range(3):
        if player == board[0][col] and player == board[1][col] and player == board[2][col]:
            draw_vert_win_line(col, player)
            return True

    for row in range(3):
        if player == board[row][0] and player == board[row][1] and player == board[row][2]:
            draw_hor_win_line(row, player)
            return True

    if player == board[2][0] and player == board[1][1] and player == board[0][2]:
        draw_asc_win_line(player)
        return True

    if player == board[0][0] and player == board[1][1] and player == board[2][2]:
        draw_desc_win_line(player)
        return True

    return False


def draw_figure():
    for row in range(3):
        for col in range(3):
            if board[row][col] == 1:
                pg.draw.line(screen, xcolor, (col * 200 + space, row * 200 + 200 - space), (col * 200 + 200 - space, row * 200 + space), kw)
                pg.draw.line(screen, xcolor, (col * 200 + space, row * 200 + space), (col * 200 + 200 - space, row * 200 + 200 - space), kw)
            elif board[row][col] == 2:
                pg.draw.circle(screen, ocolor, (int(col * 200 + 100), int(row * 200 + 100)), cr, cw)


def restart():

    global player
    for i in range(3):
        for j in range(3):
            board[i][j] = 0
    draw()
    player = 1


pg.init()
draw()

while True:

    for event in pg.event.get():

        if event.type == pg.QUIT:
            sys.exit()

        if event.type == pg.MOUSEBUTTONDOWN and not game_over:

            mouseX = event.pos[0]
            mouseY = event.pos[1]

            clicked_row = int(mouseY // 200)
            clicked_col = int(mouseX // 200)

            if available_square(clicked_row, clicked_col):

                if player == 1:
                    mark_square(clicked_row, clicked_col, 1)
                    if check_win(player):
                        game_over = True
                    player = 2

                elif player == 2:
                    mark_square(clicked_row, clicked_col, 2)
                    if check_win(player):
                        game_over = True
                    player = 1

                draw_figure()

        if event.type == pg.KEYDOWN:

            if event.key == pg.K_r:
                restart()
                game_over = False

    pg.display.update()













