import logging

from base import Point
from grid import Grid
from piece import Piece


class Pile():
    """ represent the accumulated pieces.
    """

    def append(self, piece:Piece):
        """ Append the Piece into the Pile
        """
        iter = piece.getShapeLocation()
        for p in iter:
            self.matrix[p.x][p.y] = True

    def collide(self, p:Point):
        """ Collide with Piece
        """
        if self.matrix[p.x][p.y] == True:
            return True
        return False

    def __init__(self, grid:Grid):
        self.matrix = [[False for i in range(grid.h)] for j in range(grid.w)]