import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import numpy as np
from functools import reduce
from sudoku.pro_stratigies.Cell import Cell

class Puzzle:
    def __init__(self, puzzle):
        self.grid = np.ndarray(puzzle.shape, dtype=np.object)
        for row_index, row in enumerate(puzzle):
            for col_index, cell in enumerate(row):
                self.grid[row_index][col_index] = Cell((row_index, col_index),cell)
    
    def add_single_candidate(self, block, coordinates, options):
        if (self.grid[coordinates[0],coordinates[1]].incumbent == 0):
            col = self.grid[: ,coordinates[1]]
            row = self.grid[coordinates[0], :]
            #pos_in_col = np.setdiff1d(options, col, True)
            #pos_in_row = np.setdiff1d(options, row, True)
            hints = reduce(np.union1d, (block, col, row))
            candidates = np.setdiff1d(options, hints, True) # remove hints from candidates
            candidates = np.setdiff1d(candidates, self.grid[coordinates[0],coordinates[1]].noncandidates, True) # remove any impossible candidates
            self.grid[coordinates[0],coordinates[1]].candidates = candidates
            if (len(candidates)==1): # sole candidates
                #print(candidates)
                self.grid[coordinates[0],coordinates[1]].incumbent = candidates[0]
                return True
        return False


    def __repr__(self):
        return "<Puzzle grid:%s >" % (self.grid)

    def __str__(self):
        result = self.grid
        for row_index, row in enumerate(self.grid):
            for col_index, cell in enumerate(row):
                result[row_index][col_index] = cell.incumbent
        return "%s" % (self.grid)

    def to_array(self):
        result = self.grid
        for row_index, row in enumerate(self.grid):
            for col_index, cell in enumerate(row):
                result[row_index][col_index] = cell.incumbent
        return np.array(self.grid)