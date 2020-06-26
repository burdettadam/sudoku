# The Game of Sudoku
Sudoku is a number game, where players are challenged with completing a Sudoku pattern by adding missing numbers to a large Sudoku board while abiding by a set of rules. The Sudoku board consists of a 9x9 grid with 3x3 sub-grids known as blocks containing cells with numbers between 1-9, missing cells are represented with 0's. When a cell contains a valid Sudoku number, that number is called an incumbent. All valid incumbents must satisfy the Sudoku board pattern or rule, that is.
`All rows, collumns and blocks are unique sets of incumbents with values 1-9`
several rules can be derived from that pattern that help establish new incumbents.
---
This project explores different approaches to solving Sudoku puzzles. Play with the code online with [colab](https://colab.research.google.com/drive/1bvAVmE8zWBZlmmb7G_qqBa4Jy2X0abLo?usp=sharing)
In computer science Sudoku puzzles are known to be a np-hard problem, where there is not a known scalable algorithm, but because of the small number set we are able to solve them in fractions of a second.
## Strategies
### Brute Force
Just try every possible value. That is what we call brute forcing, just trying every possible value.
A non trivial coding question often asked of programmers, "Using recursion, write a function that will verify a given cell is a valid incumbent of a provided sudoku board". 
...
"Using your incumbent verifier, solve a provided Sudoku board"

while we are using brute force we are also implementing backtick, which is try every possible path until it fails and then go back and try another.

### Human Strategy

learn more at [kristanix.com](https://www.kristanix.com/sudokuepic/sudoku-solving-techniques.php).
### Brute Force

### multiverse strategy
