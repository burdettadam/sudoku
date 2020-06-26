import numpy as np

sole_test  = np.array([ [0,0,0,  0,0,1,  0,0,0],
                        [0,0,0,  0,0,0,  0,0,0],
                        [0,0,0,  0,0,6,  0,0,0],
                      
                        [0,0,0,  4,0,0,  0,0,0],
                        [0,0,0,  0,8,0,  0,0,0],
                        [2,0,9,  0,0,0,  0,0,7],
                        
                        [0,0,0,  0,0,0,  0,0,0],
                        [0,0,0,  0,0,3,  0,0,0],
                        [0,0,0,  0,0,0,  0,0,0]])

sole_ans =  np.array([  [0,0,0,  0,0,1,  0,0,0],
                        [0,0,0,  0,0,0,  0,0,0],
                        [0,0,0,  0,0,6,  0,0,0],
                      
                        [0,0,0,  4,0,0,  0,0,0],
                        [0,0,0,  0,8,0,  0,0,0],
                        [2,0,9,  0,0,5,  0,0,7],
                        
                        [0,0,0,  0,0,0,  0,0,0],
                        [0,0,0,  0,0,3,  0,0,0],
                        [0,0,0,  0,0,0,  0,0,0]])

unique_test  = np.array([ [0,0,4,  0,0,0,  0,0,0],
                          [0,0,0,  0,0,0,  0,0,0],
                          [0,0,0,  0,0,0,  0,0,0],
                        
                          [0,0,0,  0,0,0,  0,0,0],
                          [0,4,0,  0,0,0,  0,0,0],
                          [0,0,0,  0,0,0,  0,0,0],
                          
                          [5,0,0,  0,0,0,  0,0,0],
                          [0,0,0,  0,0,0,  0,0,0],
                          [0,0,0,  0,0,4,  0,0,0]])

unique_ans  = np.array([  [0,0,4,  0,0,0,  0,0,0],
                          [0,0,0,  0,0,0,  0,0,0],
                          [0,0,0,  0,0,0,  0,0,0],
                        
                          [0,0,0,  0,0,0,  0,0,0],
                          [0,4,0,  0,0,0,  0,0,0],
                          [0,0,0,  0,0,0,  0,0,0],
                          
                          [5,0,0,  0,0,0,  0,0,0],
                          [4,0,0,  0,0,0,  0,0,0],
                          [0,0,0,  0,0,4,  0,0,0]])
row_interactions_test  = np.array([ [0,0,0,  0,7,0,  0,0,0],
                                    [0,0,0,  0,0,0,  0,0,0],
                                    [0,0,0,  0,0,0,  0,0,0],
                                  
                                    [0,0,0,  2,0,1,  0,0,0],
                                    [0,0,0,  0,0,0,  0,0,0],
                                    [0,0,0,  9,0,6,  0,0,0],
                                    
                                    [0,0,0,  0,0,0,  0,0,0],
                                    [0,0,0,  0,0,0,  0,0,0],
                                    [0,0,0,  0,0,0,  0,0,0]])

row_im_can  = np.array([[[0],[0],[0],  [0],[0],[0],  [0],[0],[0]],
                    [[0],[0],[0],  [0],[0],[0],  [0],[0],[0]],
                    [[0],[0],[0],  [0],[0],[0],  [0],[0],[0]],
                  
                    [[0],[0],[0],  [0],[0],[0],  [0],[0],[0]],
                    [[7],[7],[7],  [0],[0],[0],  [7],[7],[7]],
                    [[0],[0],[0],  [0],[0],[0],  [0],[0],[0]],
                    
                    [[0],[0],[0],  [0],[0],[0],  [0],[0],[0]],
                    [[0],[0],[0],  [0],[0],[0],  [0],[0],[0]],
                    [[0],[0],[0],  [0],[0],[0],  [0],[0],[0]],])

col_interactions_test  = np.array([ [0,0,0,  0,0,0,  0,0,0],
                                    [0,0,0,  0,0,0,  0,0,0],
                                    [0,0,0,  0,0,0,  0,0,0],
                                  
                                    [0,0,0,  1,0,6,  0,0,0],
                                    [7,0,0,  0,0,0,  0,0,0],
                                    [0,0,0,  2,0,9,  0,0,0],
                                    
                                    [0,0,0,  0,0,0,  0,0,0],
                                    [0,0,0,  0,0,0,  0,0,0],
                                    [0,0,0,  0,0,0,  0,0,0]])

col_im_can  = np.array([[[0],[0],[0],  [0],[7],[0],  [0],[0],[0]],
                        [[0],[0],[0],  [0],[7],[0],  [0],[0],[0]],
                        [[0],[0],[0],  [0],[7],[0],  [0],[0],[0]],
                    
                        [[0],[0],[0],  [0],[0],[0],  [0],[0],[0]],
                        [[0],[0],[0],  [0],[0],[0],  [0],[0],[0]],
                        [[0],[0],[0],  [0],[0],[0],  [0],[0],[0]],
                        
                        [[0],[0],[0],  [0],[7],[0],  [0],[0],[0]],
                        [[0],[0],[0],  [0],[7],[0],  [0],[0],[0]],
                        [[0],[0],[0],  [0],[7],[0],  [0],[0],[0]],])

mt  = np.array([[[0],[0],[0],  [0],[0],[0],  [0],[0],[0]],
                [[0],[0],[0],  [0],[0],[0],  [0],[0],[0]],
                [[0],[0],[0],  [0],[0],[0],  [0],[0],[0]],
              
                [[0],[0],[0],  [0],[0],[0],  [0],[0],[0]],
                [[0],[0],[0],  [0],[0],[0],  [0],[0],[0]],
                [[0],[0],[0],  [0],[0],[0],  [0],[0],[0]],
                
                [[0],[0],[0],  [0],[0],[0],  [0],[0],[0]],
                [[0],[0],[0],  [0],[0],[0],  [0],[0],[0]],
                [[0],[0],[0],  [0],[0],[0],  [0],[0],[0]],])

easy =    np.array([[5,8,0,  1,0,2,  0,4,0],
                    [0,0,0,  0,0,0,  2,1,6],
                    [9,1,0,  7,0,4,  0,0,3],
                  
                    [0,0,0,  0,2,0,  0,0,0],
                    [2,0,3,  9,1,0,  7,0,0],
                    [7,9,0,  0,0,3,  4,0,5],
                    
                    [6,0,0,  0,0,1,  5,0,4],
                    [1,5,0,  0,4,0,  6,7,2],
                    [3,0,0,  2,0,0,  0,8,9]])

easy_ans = np.array([[5, 8, 6, 1, 3, 2, 9, 4, 7,],
                    [4, 3, 7, 5, 9, 8, 2, 1, 6,],
                    [9, 1, 2, 7, 6, 4, 8, 5, 3,],
                    [8, 6, 5, 4, 2, 7, 3, 9, 1,],
                    [2, 4, 3, 9, 1, 5, 7, 6, 8,],
                    [7, 9, 1, 6, 8, 3, 4, 2, 5,],
                    [6, 2, 9, 8, 7, 1, 5, 3, 4,],
                    [1, 5, 8, 3, 4, 9, 6, 7, 2,],
                    [3, 7, 4, 2, 5, 6, 1, 8, 9,]])

medium =  np.array([[7,6,0,  0,0,0,  0,0,0],
                    [0,1,0,  0,6,2,  0,0,0],
                    [0,0,8,  0,0,4,  0,0,0],
                  
                    [5,0,0,  8,2,7,  0,0,0],
                    [0,3,1,  0,0,9,  2,0,0],
                    [0,0,2,  5,3,0,  9,0,0],
                    
                    [0,5,0,  0,9,0,  8,0,0],
                    [0,0,0,  0,0,0,  7,0,5],
                    [2,0,4,  7,0,0,  1,9,6]])

hard =  np.array([[0,0,5,  0,0,0,  0,0,0],
                  [0,0,2,  4,0,1,  0,7,0],
                  [3,0,4,  0,0,0,  5,6,0],
                
                  [0,0,0,  0,0,0,  0,0,0],
                  [0,0,0,  0,0,7,  9,8,4],
                  [8,0,0,  0,9,0,  0,1,0],
                  
                  [0,0,0,  2,0,0,  1,0,0],
                  [0,9,0,  0,7,0,  0,0,2],
                  [0,1,8,  3,0,0,  0,4,0]])