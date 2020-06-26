import os
import pytest
from .context import sudoku, validate
from sudoku import sudoku
from .starts import easy, easy_ans

def test_easy():
    solution = sudoku.solve(easy).to_array()
    print("Solution",solution)
    assert validate(solution)
    