import pygame
import sys
import random
from pygame.locals import *

from piece import I, J, L, O, S, T, Z, Vector, Rotate
from grid import Grid
from base import Point
from pile import Pile


X=10
Y=20

pygame.init()
pygame.display.set_caption("Python Teteris")
pygame.font.init()
over_font = pygame.font.Font(pygame.font.get_default_font(), 36)
over_text = pygame.font.Font.render(over_font, 'Game Over', True, (0, 255, 255))
pygame.key.set_repeat(300, 10)
clock = pygame.time.Clock()
grid = Grid(X, Y)
pile = Pile(grid)
all_cubes = [I, J, L, O, S, T, Z]

active = None
# set a timer for every 1 second initial
pygame.time.set_timer(pygame.USEREVENT, 1000)



while True:
    clock.tick(10)

    move = Point(0, 0)
    if active is None:
        active = all_cubes[random.randint(0, 6)](Point(4, 1))
        # active = T(Point(4, 1))
        if pile.collideWithPiece(active):
            # Print Game Over
            grid.text(over_text)
            active = None
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                move = Vector.VT_UP
            if event.key == pygame.K_s:
                move = Vector.VT_DOWN
            if event.key == pygame.K_d:
                move = Vector.VT_RIGHT
            if event.key == pygame.K_a:
                move = Vector.VT_LEFT
            if event.key == pygame.K_COMMA:
                move = Rotate.ROT_COUNTERCLOCK
            if event.key == pygame.K_PERIOD:
                move = Rotate.ROT_CLOCK
        if event.type == pygame.USEREVENT:
            move = Vector.VT_DOWN

    if active and move != Point(0,0):
        active = active.move(grid, move, pile)

    
    pygame.display.flip()
    pygame.display.update()

