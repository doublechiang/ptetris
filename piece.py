import abc
import enum
from typing import List

from base import Point


class Rotate(enum.IntEnum):
    ROT_CLOCK=-1,
    ROT_COUNTERCLOCK=1

class Vector(enum.Enum):
    VT_RIGHT=Point(1,0)
    VT_LEFT=Point(-1, 0)
    VT_DOWN=Point(0,1)
    VT_UP=Point(0,-1)


class Piece:
    def move(self, grid, move, pile):
        """ move, rotatate the piece
            return self is the moving object success
            return False if the move result in the instance vanish
        """

        new_shape = self.__getNewShape(move)
        for b in new_shape:
            if grid.isInside(b) is False:
                if move == Vector.VT_DOWN:
                    pile.append(self)
                    pile.update(grid)
                    return None
                return self

        for b in new_shape:
            if pile.collide(b):
                pile.append(self)
                pile.update(grid)
                return None

        # erase previous background 
        self.draw(grid, (0, 0, 0))
        # draw the new location
        if isinstance(move, Vector):
            self.pos = self.pos + move

        if isinstance(move, Rotate):
            self.shape_idx = (self.shape_idx + move) % len(self.pattern)
            self.shape = self.pattern[self.shape_idx] 
        self.draw(grid)
        return self



    def __getNewShape(self, move):
        """ return the list of new position 
        """
        if isinstance(move, Point) or isinstance(move, Vector):
            return list(map(lambda x: self.pos + x + move, self.shape))
        if isinstance(move, Rotate):
            new_idx = (self.shape_idx + move) % len(self.pattern)
            new_shape = self.pattern[new_idx]
            return list(map(lambda x: self.pos + x, new_shape))
        return None



    def draw(self, grid, color=None):
        if color == None:
            color = self.color
        grid.drawRect(color, self.pos)
        for t in self.shape:
            offset = self.pos + t
            grid.drawRect(color, offset)

    def getShapeLocation(self)-> List[Point]:
        return map(lambda x: x+ self.pos,  self.shape)


    def __init__(self, point:Point):
        self.pos =point
        # define a type without value
        self.pattern: list
        self.shape: list
        self.shape_idx = None


class I(Piece):
    SHAPE = [
        [Point(-1,0), Point(0, 0), Point(1,0), Point(2,0)],
        [Point(0, -1), Point(0, 0), Point(0, 1), Point(0, 2)]
    ]

    def __init__(self, point):
        super().__init__(point)
        self.color = (255, 0, 0)
        self.shape_idx = 0
        self.pattern = I.SHAPE
        self.shape = I.SHAPE[self.shape_idx]

class J(Piece):
    SHAPE = [
        [Point(0,-1), Point(0, 0), Point(1,0), Point(2,0)],
        [Point(-1, 0), Point(0, 0), Point(0, -1), Point(0, -2)],
        [Point(-2, 0), Point(-1, 0), Point(0, 0), Point(0, 1)],
        [Point(0, 0), Point(0, 1), Point(0, 2), Point(1, 0)]
    ]
    def __init__(self, point):
        super().__init__(point)
        self.color = (255, 0, 0)
        self.shape_idx = 0
        self.pattern = J.SHAPE
        self.shape = J.SHAPE[self.shape_idx]



class L(Piece):
    SHAPE = [
        [Point(0,0), Point(1, 0), Point(2,0), Point(2,-1)],
        [Point(-1, 0), Point(0, 0), Point(0, 1), Point(0, 2)],
        [Point(0, 0), Point(1, 0), Point(2, 0), Point(0, 1)],
        [Point(0, -2), Point(0, -1), Point(0, 0), Point(1, 0)]
    ]
    def __init__(self, point):
        super().__init__(point)
        self.color = (255, 0, 0)
        self.shape_idx = 0
        self.pattern = L.SHAPE
        self.shape = L.SHAPE[self.shape_idx]

class O(Piece):
    SHAPE = [
        [Point(0,0), Point(1, 0), Point(0,1), Point(1,1)],
    ]
    def __init__(self, point):
        super().__init__(point)
        self.color = (255, 0, 0)
        self.shape_idx = 0
        self.pattern = O.SHAPE
        self.shape = O.SHAPE[self.shape_idx]

class S(Piece):
    SHAPE = [
        [Point(-1,0), Point(0, 0), Point(0, -1), Point(1, -1)],
        [Point(-1, 0), Point(-1, -1), Point(0, 0), Point(0, 1)]
    ]
    def __init__(self, point):
        super().__init__(point)
        self.color = (255, 0, 0)
        self.shape_idx = 0
        self.pattern = S.SHAPE
        self.shape = S.SHAPE[self.shape_idx]

class T(Piece):
    SHAPE = [
        [Point(-1,0), Point(0, 0), Point(1,0), Point(0,-1)],
        [Point(-1, 0), Point(0, 0), Point(0, 1), Point(0, -1)],
        [Point(-1, 0), Point(0, 0), Point(1, 0), Point(0, 1)],
        [Point(0, -1), Point(0, 0), Point(0, 1), Point(1, 0)]
    ]
    def __init__(self, point):
        super().__init__(point)
        self.color = (255, 0, 0)
        self.shape_idx = 0
        self.pattern = T.SHAPE
        self.shape = T.SHAPE[self.shape_idx]

class Z(Piece):
    SHAPE = [
        [Point(-1,0), Point(0, 0), Point(0,1), Point(1,1)],
        [Point(-1, 0), Point(0, 0), Point(0, 1), Point(0, 2)],
        [Point(0, 0), Point(1, 0), Point(2, 0), Point(0, 1)],
        [Point(-1, 0), Point(-1, 1), Point(0, 0), Point(0, -1)]
    ]
    def __init__(self, point):
        super().__init__(point)
        self.color = (255, 0, 0)
        self.shape_idx = 0
        self.pattern = Z.SHAPE
        self.shape = Z.SHAPE[self.shape_idx]


