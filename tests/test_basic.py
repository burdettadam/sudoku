
import os
import pytest
from .context import sudoku
from sudoku.core.Sudoku import Sudoku
#from Sudoku import Sudoku
from .starts import *

def test_sole_candidate():
    puzzle = Sudoku(sole_test)
    puzzle.track_candidates()
    solution = puzzle.to_array()
    for row_index, row in enumerate(solution):
        for col_index, cell in enumerate(row):
            assert cell == sole_ans[row_index][col_index]
    
def test_unique_candidate():
    puzzle = Sudoku(unique_test)
    puzzle.track_candidates()
    solution = puzzle.to_array()
    print(solution)
    for row_index, row in enumerate(solution):
        for col_index, cell in enumerate(row):
            assert cell == unique_ans[row_index][col_index]
    
def test_row_elimination_candidate():
    solution = Sudoku(unique_test)
    solution.track_candidates()
    for row_index, row in enumerate(solution.grid):
        for col_index, cell in enumerate(row):
            assert len(cell.noncandidates) == len(row_im_can[row_index][col_index])
            for candidate in cell.noncandidates:
                assert candidate in row_im_can[row_index][col_index]
    
def test_col_elimination_candidate():
    solution = Sudoku(unique_test)
    solution.track_candidates()
    for row_index, row in enumerate(solution.grid):
        for col_index, cell in enumerate(row):
            assert len(cell.noncandidates) == len(col_im_can[row_index][col_index])
            for candidate in cell.noncandidates:
                assert candidate in row_im_can[row_index][col_index]
def test_x_wing_elimination():
    pass

def test_is_symmetric():
    pass