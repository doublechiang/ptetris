import pygame
import sys
from pygame.locals import *

from piece import I, L
from grid import Grid


X=50
Y=100
SCALE=10
DISPLAYSURF = pygame.display.set_mode((X*SCALE, Y*SCALE))

pygame.init()
while True:
    grid = Grid(DISPLAYSURF)
    p = I((0,2))
    p.draw(grid)

    p = L((5,4))
    p.draw(grid)

    
    

    pygame.display.flip()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)