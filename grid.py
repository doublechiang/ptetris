import pygame

class Grid:
    SCALE=50

    def drawRect(self, color, co):
        x = co[0]
        y = co[1]
        rect = pygame.Rect(x*50, y*50, 50, 50)
        pygame.draw.rect(self.surface, color, rect)

    def setSurface(self, surface):
        self.surface = surface

    def __init__(self, tuple):
        self.w = tuple[0]
        self.h = tuple[1]
        self.surface = pygame.display.set_mode((self.w * Grid.SCALE, self.h * Grid.SCALE))
