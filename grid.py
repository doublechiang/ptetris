import pygame
from base import Point

class Grid:
    SCALE=50

    def drawRect(self, color, point:Point):
        x = point.x
        y = point.y
        rect = pygame.Rect(x*Grid.SCALE, y*Grid.SCALE, Grid.SCALE, Grid.SCALE)
        pygame.draw.rect(self.surface, color, rect)

    def setSurface(self, surface):
        self.surface = surface

    def isInside(self, point:Point):
        """ if the point still inside the grid 
            return True or False
        """
        if point.x < 0 or point.x >= self.w:
            return False
        if point.y < 0 or point.y >= self.h:
            return False
        return True


    def __init__(self, width, height):
        self.w = width
        self.h = height
        self.surface = pygame.display.set_mode((self.w * Grid.SCALE, self.h * Grid.SCALE))
