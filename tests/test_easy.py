import os
import pytest
from .context import sudoku
from sudoku import sudoku
from .starts import easy, easy_ans

def test_easy():
    solution = sudoku.solve(easy).to_array()
    for row_index, row in enumerate(solution):
        for col_index, cell in enumerate(row):
            assert cell == easy_ans[row_index][col_index]
    