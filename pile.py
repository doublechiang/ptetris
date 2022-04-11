import logging
import numpy as np

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
            self.matrix[p.y][p.x] = True
        logging.debug(self.matrix)

    def collide(self, p:Point):
        """ Collide with Piece
        """
        if self.matrix[p.y][p.x] == True:
            logging.debug(self.matrix)
            return True
        return False

    def __remove_row(self, row, grid):
        # y is the row all occupied
        new_matrix = np.delete(self.matrix, row, 0)
        new_matrix = np.insert(new_matrix, 0, np.array([False for i in range(grid.w)]), axis=0)
        diff = new_matrix ^ self.matrix

        # erase/draw any changes
        changes = np.where(diff==True)
        if len(changes) != 1:
            list_changes = list(zip(changes[1], changes[0]))
            for cell in list_changes:
                p = Point(cell[0], cell[1])
                action = new_matrix[p.y][p.x]
                color  = (0,0,0)
                if action:
                    color = (255,0,0)
                grid.drawRect(color, p)
            self.matrix = new_matrix



    def update(self, grid):
        """ Check if any rows are all occupied then delete it.
            Since could have multiple row erase, recursive call till no more occupied
        """
        diff = np.array([])
        for y in range(0, len(self.matrix)):
            if False in self.matrix[y, :]:
                continue
            self.__remove_row(y, grid)

        # all processed 


    def __init__(self, grid:Grid):
        self.matrix = np.array([[False for i in range(grid.w)] for j in range(grid.h)])