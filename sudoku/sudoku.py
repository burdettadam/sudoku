import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from sudoku.pro_stratigies.Puzzle import Puzzle
from tests import starts
import numpy as np


def add_single_candidates(puzzle):
    for block_row_idx in [0,3,6]:
        for block_col_idx in [0,3,6]: #todo: remove hardcoded value
            block = puzzle.grid[block_row_idx:block_row_idx + 3, block_col_idx:block_col_idx + 3]
            block = block.flatten() # hints in block
            #print("block",block)
            for r in range(3):
                for c in range(3):
                    if puzzle.add_single_candidate(block, (block_row_idx + r, block_col_idx + c), np.array(range(1,9+1))):
                        return True , puzzle #restart adding single candidates
    return False , puzzle
added_candidate = True

def solve(puzzle):
    puzzle = Puzzle(puzzle)
    found_candidate = True
    while(found_candidate):
        found_candidate, puzzle = add_single_candidates(puzzle)
    return puzzle

print(solve(starts.easy))
