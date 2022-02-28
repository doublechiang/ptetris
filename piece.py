import pygame

class Piece:
    def move(self):
        pass

    def draw(self, grid):
        grid.drawRect(self.color, self.pos)
        for t in self.shape:
            x = self.pos[0] + t[0]
            y = self.pos[1] + t[1]
            grid.drawRect(self.color, (x,y))

    def __init__(self, tuple):
        self.pos = tuple


class I(Piece):
    def __init__(self, tuple):
        super().__init__(tuple)
        self.color = (255, 0, 0)
        self.shape = [(1,0), (2,0), (3,0)]

class L(Piece):
    def __init__(self, tuple):
        super().__init__(tuple)
        self.color = (0, 255, 0)
        self.shape = [(0,1), (1,1), (2,1)]

