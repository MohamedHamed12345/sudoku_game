import random
import time


from file_operations import read_board , write_board
BOARD_SIZE = 9

# Define the number of squares to remove for each difficulty level
d={
'easy' :30,
'medium' : 45,
'hard' : 60,
'extreme' :75,
}


def get_sudoku(sudoku):
   
    for row in range(9):
        for col in range(9):
            if sudoku[row][col] == 0:
                nums = list(range(1, 10))
                random.shuffle(nums)
                for num in nums:
                    if (num not in sudoku[row] and 
                        num not in [sudoku[i][col] for i in range(9)] and
                        num not in [sudoku[i][j] for i in range(row//3*3, row//3*3+3) for j in range(col//3*3, col//3*3+3)]):
                        sudoku[row][col] = num
                        if get_sudoku(sudoku):
                            return True
                        sudoku[row][col] = 0
                return False
    return True  

def get_difficulty_level():
   
    while True:
        level = input('Please select difficulty level (easy, medium, hard, or extreme) or exit : ').lower()
        if level in d: return d[level]
        elif level =='exit':exit()
        else: print('Invalid input, please try again.')
           
def remove_squares(board, num_squares):
    """Remove a specified number of squares from the board."""
    squares = list(range(BOARD_SIZE ** 2))
    random.shuffle(squares)
    for i in range(num_squares):
        square = squares[i]
        row = square // BOARD_SIZE  #1 to 9 only
        col = square % BOARD_SIZE   ##1 to 9 only
        board[row][col] = " "

def check_solution(board,remboard):
    for i in range(9):
        for j in range(9):
            if remboard[i][j]!=' ' and  board[i][j]!= remboard[i][j]:
                print('you change the numbers')
                return False
    rows = {}
    cols ={}
    board3x3 ={}
    for i in range(9):rows[i]=[];cols[i]=[]

    for i in range(3):
        for j in range(3):board3x3[(i,j)]=[]

    for i in range(9): 
        for j in range(9):
            element=board[i][j]
            
 
            if  (element in rows[i] )or (element in cols[j]) or element in board3x3[(i//3,j//3)]:return False
            rows[i].append(board[i][j])
            cols[j].append(board[i][j])
            board3x3[(i//3, j//3)].append(board[i][j])
    return True


def ask(board):
    x=input('do you want to see the answer Y or N ? ')
    if x.lower()=='y':
        print('You can see the answer in file  ')
        write_board(board,'solution.txt')
   

def main():

    board = [[0]*9 for _ in range(9)]
    get_sudoku(board)
    write_board(board,'gamesolution.txt')
    ref=[i[:] for i in board]
    level = get_difficulty_level()
    remove_squares(board, level)
    print('you can write your solution in solution file with this root ')
    write_board(board,'sudoku_game.txt')
    
   
    start = time.time()
    x=input('enter  y after finish or exit ')
    if x=='exit':exit()
    end = time.time()
    readedboard=read_board()
    print(f"time taken :{round(end-start,3)} seconds")
    if len(readedboard) !=9:
     
        ask(ref)
        return

    if check_solution(readedboard,board):
        print("right solution")

    else: 
        print('wrong solution')
        ask(ref)
   



if __name__=="__main__":    
    try:
        main()
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
        print('Game over')
        exit()
    except ValueError():
        print("value error")
        print("there are unfonund value")
        print('Game over')
        exit()
    while True:
        try:
            x=input('Do you want to play again :Y or N ?')
            if x.lower()=='y':
           
                main()
        except KeyboardInterrupt:
                print('Game over')
                exit()
        else:
            print('Game over')
            break