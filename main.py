import pygame
import sys
from pygame.locals import *

from piece import I, L
from grid import Grid


X=10
Y=20

pygame.init()
grid = Grid((X, Y))
p = I((0,2))
p.draw(grid)

while True:
 
    pygame.display.flip()
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                p.move(grid, (0, -1))
            if event.key == pygame.K_s:
                p.move(grid, (0, 1))
            if event.key == pygame.K_d:
                p.move(grid, (1, 0))
            if event.key == pygame.K_a:
                p.move(grid, (-1, 0))
            # if event.key == pygame.K_q:
            #     pygame.quit()
            #     sys.exit(0)
            if event.key == pygame.K_COMMA:
                pass
            if event.key == pygame.K_PERIOD:
                pass
    
