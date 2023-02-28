import sudoku

def write_board(board,filename):
  
    file=open(filename,'w')
    h1="".join((" "+" ".join(['-'*9 for _ in range(3)])+" ") for i in range(3))+'\n'
    h2="".join(("|"+"|".join([' '*9 for _ in range(3)])+"|") for i in range(3))+'\n'
    for h in range(3):
        for k in range(3):
            file.write(h1+h2*2)
            tmp="".join(("|"+"|".join(['    '+f"{board[h*3+k][j*3+i]}"+'    ' for i in range(3)])+"|") for j in range(3))+'\n'
            file.write(tmp)
            file.write(h2*2)
        file.write(h1)
    print(__file__.replace("file_operations.py",filename))             
                 
def read():
    file=open('sudoku_game.txt','r',encoding='utf-8',errors='ignore')
    ze_lines=file.read().splitlines()
    board=[]
    l=[]
    for line in ze_lines:
        for i in line:
            if i.isdigit()==True:
                l.append(i)
    j=0
    x=[]
    while j<81:
        
        if(len(x)==9):
            x=[]
        for i in range(9):
            x.append(l[j])
            j+=1
        board.append(x) 
    return board
                
            

def main():
    
  board = sudoku.create_board()

  sudoku.fill_sudoku(board)
  correct_ans = []

  for row in board:
    new_row = []
    for item in row:
        new_row.append(item)
    correct_ans.append(new_row)

  level = sudoku.get_difficulty_level()

  if level == 'easy':
    sudoku.remove_squares(board, sudoku.EASY_SQUARES)
  elif level == 'medium':
     sudoku.remove_squares(board, sudoku.MEDIUM_SQUARES)
  elif level == 'hard':
    sudoku.remove_squares(board, sudoku.HARD_SQUARES)
  else:
     sudoku.remove_squares(board, sudoku.EXTREME_SQUARES)
  write_board(board,'sudoku_game.txt')    
  x=input(" enter y if you have finish : ")
  if x == 'y':
     user_sol=read()
  flag=sudoku.check_solution(user_sol)  
  if flag== True:
     print("your sol is true")
  elif flag== False:
     print("your sol is false")
  ask=input("do you want the answer: y or n")
  if ask=='y':
     write_board(correct_ans, "solution.txt")
     
  else:
     print("as you like ya غالي ")
 
     
 
 
main() 
 
 
 
 
 
 
 
 
 
 
 