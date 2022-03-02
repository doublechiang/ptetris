import pygame

class Piece:
    def move(self, grid, movement):
        x, y = self.pos[0], self.pos[1]
        # check if over boundary
        dim = self.getDim()
        if movement[0] > 0:
            dest_x = x + dim[2] + movement[0]
            if dest_x >= grid.w:
                return False
        if movement[0] < 0:
            dest_x = x + dim[0] + movement[0]
            if dest_x <0:
                return False

        if movement[1] > 0:
            dest_y = y + dim[1] + movement[1]
            if dest_y >= grid.h:
                return False
        if movement[1] < 0:         # move up
            dest_y = y + dim[3] + movement[1]
            if dest_y < 0:
                return False

        self.draw(grid, (0, 0, 0))
        x += movement[0]
        y += movement[1]
        self.pos=(x, y)
        self.draw(grid)
        return True

    def draw(self, grid, color=None):
        if color == None:
            color = self.color
        grid.drawRect(color, self.pos)
        for t in self.shape:
            x = self.pos[0] + t[0]
            y = self.pos[1] + t[1]
            grid.drawRect(color, (x,y))

    def getDim(self):
        """ Return tuple contain size to postion
        """
        max_x = min_x = max_y = min_y = 0
        for t in self.shape:
            max_x = max(max_x, t[0])
            min_x = min(min_x, t[0])
            max_y = max(max_y, t[1])
            min_y = min(min_y, t[1])
        return (min_x, min_y, max_x, max_y)
     

    def __init__(self, co):
        self.pos = co


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

