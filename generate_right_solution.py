import random
def ifNumIsValid(sudoku,row,col,num):
    #function to check if generated number is valid
    if num in sudoku[row]:
        return False
    if num  in [sudoku[i][col] for i in range(0,9)]:
        return False
    if num  in [sudoku[i][j] for i in range(row//3*3,row//3*3+3) for j in range(col//3*3,col//3*3+3)]:
        return False
    if sudoku[row][col]!=0 :
        return False 
    return True


def generate_right_solution(sudoku):
    for row in range(9):
        for col in range(9):
                  num=random.randint(1,9)
                  if(ifNumIsValid(sudoku, row, col, num)==True):
                      sudoku[row][col]=num