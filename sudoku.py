
import random

BOARD_SIZE = 9

# Define the number of squares to remove for each difficulty level
EASY_SQUARES = 30
MEDIUM_SQUARES = 45
HARD_SQUARES = 60
EXTREME_SQUARES = 75


def create_board():
    board=[]
    for i in range(9):
        x=[]
        for i in range(9):
            x.append(0)
        board.append(x)
    return board


def fill_sudoku(sudoku):
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
                        if fill_sudoku(sudoku):
                            return True
                        sudoku[row][col] = 0
                return False
    return True
#called in text file by give it board from previous function 

def print_board(board):
    """Print the Sudoku board."""
    print('-' * 35)
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            print(board[i][j], end='  ')
            if (j + 1) % 3 == 0 and j != BOARD_SIZE - 1:
                print('||', end='  ')
            
        print()
        print()
        if (i + 1) % 3 == 0 and i != BOARD_SIZE - 1:
            print('-' * 35)
    print('-' * 35)       


def get_difficulty_level():
    """Get the difficulty level from the user."""
    while True:
        level = input('Please select difficulty level (easy, medium, hard, or extreme): ').lower()
        if level in ['easy', 'medium', 'hard', 'extreme']:
            return level
        else:
            print('Invalid input, please try again.')


def remove_squares(board, num_squares):
    """Remove a specified number of squares from the board."""
    squares = list(range(BOARD_SIZE ** 2))
    random.shuffle(squares)
    for i in range(num_squares):
        square = squares[i]
        row = square // BOARD_SIZE  #1 to 9 only
        col = square % BOARD_SIZE   ##1 to 9 only
        board[row][col] = "#"

if __name__=="__main__":
    
 board = create_board()
 fill_sudoku(board)
 
 level = get_difficulty_level()

 if level == 'easy':
    remove_squares(board, EASY_SQUARES)
 elif level == 'medium':
     remove_squares(board, MEDIUM_SQUARES)
 elif level == 'hard':
    remove_squares(board, HARD_SQUARES)
 else:
     remove_squares(board, EXTREME_SQUARES)
 
 print_board(board)











