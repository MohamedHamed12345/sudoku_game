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
    
def genertaeRandom():
    #this function to generate random numbers in a board from 4 different levels
    print("choose the level of the game:-\n","1-Easy \n 2-mediam \n 3-hard \n 4-extreme")
    choice=int(input("your choice : "))
    sudoku=[[0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            ]
    position=[0,1,2,3,4,5,6,7,8]
    if choice ==1 :
        i=0
        while i<=34:
                  row= random.choice(position)
                  col= random.choice(position)
                  num=random.randint(1,9)
                  if(ifNumIsValid(sudoku, row, col, num)==True):
                      sudoku[row][col]=num
                      i+=1
                    
        print(sudoku)
    if choice ==2 :
        i=0
        while i<=24:
                  row= random.choice(position)
                  col= random.choice(position)
                  num=random.randint(1,9)
                  if(ifNumIsValid(sudoku, row, col, num)==True):
                      sudoku[row][col]=num
                      i+=1
                  
        print(sudoku)
        
    if choice ==3 :
        i=0
        while i<=14:
                  row= random.choice(position)
                  col= random.choice(position)
                  num=random.randint(1,9)
                  if(ifNumIsValid(sudoku, row, col, num)==True):
                      sudoku[row][col]=num
                      i+=1
        print(sudoku)
        
    if choice ==4 :
        i=0
        while i<=4:
                  row= random.choice(position)
                  col= random.choice(position)
                  num=random.randint(1,9)
                  if(ifNumIsValid(sudoku, row, col, num)==True):
                      sudoku[row][col]=num
                      i+=1
        print(sudoku)
    return sudoku

sudoku=genertaeRandom()
