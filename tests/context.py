import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import numpy as np
import sudoku

def validate(puzzle):
    '''
    there actually is a way, using only arithmetic, to check whether a sequence of 
    nine numbers each between 1 and 9 contains all unique elements: for each number 
    𝑛 in the sequence, replace it with 2𝑛−1, then add them all up and check that the 
    sum is 511. For example, the row [5|3|4|6|7|8|9|1|2] is valid because
    25−1+23−1+24−1+26−1+27−1+28−1+29−1+21−1+22−1=16+4+8+32+64+128+256+1+2=511, 
    It should be clear that any permutation of the same set of numbers should give 
    the same sum, so any valid solution should have the sum 511. What is not 
    immediately obvious is that no other sequence of nine numbers can give this sum. 
    This is true because the Hamming weight of 511 is 9. The sum of 𝑁 numbers that 
    are powers of 2 can have Hamming weight at most 𝑁, and if there are duplicates 
    among them, the weight of the sum is strictly less than 𝑁. So the only way to 
    get a Hamming weight of 9 by adding nine powers of 2 is if they are all distinct.
    -https://math.stackexchange.com/a/157716
    '''
    
    def bit_sum(unique_set):
        print("unique set",unique_set)
        return np.sum(np.exp2(np.fromiter(map(lambda n: n-1, unique_set), dtype=np.int)))

    def duplicates(L):
        # source: https://stackoverflow.com/a/9836685
        seen = set()
        seen2 = set()
        seen_add = seen.add
        seen2_add = seen2.add
        for item in L:
            if item in seen:
                seen2_add(item)
            else:
                seen_add(item)
        return list(seen2)
    # the summed value of unique set of candidates, being the exponential value of 2.
    unique_bit_sum = np.sum(np.exp2(range(len(puzzle[0])))) # since index is 0 based we don't have to -1
    #check row
    for row in puzzle:
        row_sum = bit_sum(row)
        if( row_sum != unique_bit_sum):
            print("not a unique row %s, duplicates %s" % (row,duplicates(row)))
            return False
    #check col
    for col in puzzle.T:
        col_sum = bit_sum(col)
        if(col_sum != unique_bit_sum):
            print("not a unique col %s, duplicates %s" % (col,duplicates(col)))
            return False
    #check square
    for block_row_idx in [0,3,6]: #Todo: remove hardcoded..
        for block_col_idx in [0,3,6]: 
            block = puzzle[block_row_idx:block_row_idx + 3, block_col_idx:block_col_idx + 3]
            block = block.flatten() # incumbents in block
            block_sum = bit_sum(block)
            if(block_sum != unique_bit_sum):
                print("not a unique block %s, duplicates %s" % (block,duplicates(block)))
                return False
    return True

