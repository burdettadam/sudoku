from .core.Sudoku import Sudoku
from tests import starts #Todo: remove this after testing
import numpy as np


def solve(puzzle):
    """
    Given a 9x9 sudoku starting array, attempts to add all single candidates, 
    restarting after adding one. Once all single candidates are added, narrow
    search space by removing impossible candidates, then add single candidates again.
    input: 9x9 np.array() of ints ranging from 0-9, 0 being unsolved, all others being
    solved incumbents.
    output: Puzzle object containing 9x9 matrix of incumbents
    """
    puzzle = Sudoku(puzzle)
    found_candidate = True
    while(found_candidate):
        found_candidate = puzzle.track_candidates()
    return puzzle

print(solve(starts.easy))
