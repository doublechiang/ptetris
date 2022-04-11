import pygame
import sys
from pygame.locals import *

from piece import I, L, Vector, Rotate
from grid import Grid
from base import Point
from pile import Pile


X=10
Y=20

pygame.init()
pygame.key.set_repeat(300, 50)
grid = Grid(X, Y)
pile = Pile(grid)

active = I(Point(4,0))
active.draw(grid)
while True:
    move = Point(0, 0)
    if active is None:
        active = I (Point(4, 0))
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
    if active and move != Point(0,0):
        active = active.move(grid, move, pile)

    
    pygame.display.flip()
    pygame.display.update()

