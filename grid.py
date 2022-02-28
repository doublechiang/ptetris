import pygame

class Grid:

    def drawRect(self, color, tuple):
        x = tuple[0]
        y = tuple[1]
        rect = pygame.Rect(x*50, y*50, 50, 50)
        pygame.draw.rect(self.surface, color, rect)

    def setSurface(self, surface):
        self.surface = surface

    def __init__(self, surface):
        self.surface = surface