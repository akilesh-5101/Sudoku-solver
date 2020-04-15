#Variables used in the program

#Variables to input puzzle
input_line_number = 0
input_grid = ["", "", "", "", "", "", "", "", ""]

copy_row = -1
copy_column = 0


#Variables for the program to run

sudoku_lists = [["", "", "", "", "", "", "", "", ""],
               ["", "", "", "", "", "", "", "", ""],
               ["", "", "", "", "", "", "", "", ""],
               ["", "", "", "", "", "", "", "", ""],
               ["", "", "", "", "", "", "", "", ""],
               ["", "", "", "", "", "", "", "", ""],
               ["", "", "", "", "", "", "", "", ""],
               ["", "", "", "", "", "", "", "", ""],
               ["", "", "", "", "", "", "", "", ""]]
sudoku_check = []
puz_done = "not done"
ret_val = 0
sudoku_ret_val = []
f = 0
sudoku_dup = []
a = 0


#Code to input the puzzle: 
with open("puzzle_input.txt") as puzin:
    for line in puzin:
        input_grid[input_line_number] = line.rstrip()
        input_line_number += 1

for copy_row in range(9):
    for copy_column in range(9):
        sudoku_lists[copy_row][copy_column] = int(input_grid[copy_row][copy_column])
 

        

#Program Code:
import copy
from IPython.core.debugger import Pdb
ipdb = Pdb()
from sudoku_functions import *
while check_puzzle_full(sudoku_lists) == 0:
    f += 1
    sudoku_check = copy.deepcopy(sudoku_lists)
    sudoku_dup = copy.deepcopy(sudoku_lists)

    sudoku_ret_val = copy.deepcopy(puz_procedure(sudoku_lists))
    sudoku_lists = copy.deepcopy(sudoku_ret_val[0])

    #To invoke assume_solver():
    if sudoku_check == sudoku_lists:    
        for r in range(1, 10):
            for c in range(1, 10):
                if sudoku_dup[r-1][c-1] == 0:
                    a += 1
                    box = return_box(sudoku_dup,r,c)
                    col = return_col(sudoku_dup,c)
                    poss_outcome = find_possible_values(sudoku_dup,r,col,box).copy()
                    sudoku_ret_val = copy.deepcopy(assume_solver(sudoku_dup,poss_outcome,r,c))
                    sudoku_dup = copy.deepcopy(sudoku_ret_val[0])
                    ret_val = sudoku_ret_val[1]
                    if ret_val == 1:
                        sudoku_lists = copy.deepcopy(sudoku_dup)


                        
    if check_puzzle_full(sudoku_lists) == 1:
        puz_done = "dondonakadone"
        break
    if sudoku_check == sudoku_lists:
        break
                        
print(f)                        
print(ret_val)    
print(puz_done)

#To print output:

print_output(sudoku_lists)

#***********************************'
    
    







    

        


    



 
