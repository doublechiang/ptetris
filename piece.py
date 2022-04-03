import pygame

from base import Point

class Piece:
    def move(self, grid, move):

        # Check if the move still inside the grid.
        new_pos = self.pos + move
        for r in self.shape:
            p = new_pos + r
            if grid.isInside(p) is False:
                return False


        # erase previous background 
        self.draw(grid, (0, 0, 0))
        self.pos += move
        # draw the new location
        self.draw(grid)
        return True

    def draw(self, grid, color=None):
        if color == None:
            color = self.color
        grid.drawRect(color, self.pos)
        for t in self.shape:
            offset = self.pos + t
            grid.drawRect(color, offset)


    def __init__(self, point:Point):
        self.pos =point


class I(Piece):
    def __init__(self, point):
        super().__init__(point)
        self.color = (255, 0, 0)
        self.shape = [Point(0, 0), Point(1,0), Point(2,0), Point(3,0)]

class L(Piece):
    def __init__(self, tuple):
        super().__init__(tuple)
        self.color = (0, 255, 0)
        self.shape = [Point(0, 0), Point(0,1), Point(1,1), Point(2,1)]

