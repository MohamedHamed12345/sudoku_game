def read_board():
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
            x.append(int(l[j]))
            j+=1
        board.append(x) 
    # print(board)
    return board

# def read_board():
#     grid=[]
#     file=open('sudoku_game.txt', 'r')
#     for line in file:
#         if '-' in line:break
#     lst=[-1]*9
#     for l in file: 
#         line=l.replace('||','|').replace(' ','').strip()[1:-1].split('|')
    
#         if '-' in line[0]:
#             # if -1 in lst:
#             #     return ["unfound value "]
#             grid.append(lst);lst=[-1]*9
#             if len(grid)%3==0:file.readline()
#             continue
        
#         for idx, unti in enumerate(line):
#             u=unti.strip()
#             if  u=='' :    continue
#             # if not u.isdigit():
#             #     return ["value not a number"]
#             lst[idx]=int(u)
#     return grid 

def write_board(grid,filename):
    file=open(filename,'w')
    h1="".join((" "+" ".join(['-'*9 for _ in range(3)])+" ") for i in range(3))+'\n'
    h2="".join(("|"+"|".join([' '*9 for _ in range(3)])+"|") for i in range(3))+'\n'
    for h in range(3):
        for k in range(3):
            file.write(h1+h2*2)
            tmp="".join(("|"+"|".join(['    '+f"{grid[h*3+k][j*3+i]}"+'    ' for i in range(3)])+"|") for j in range(3))+'\n'
            file.write(tmp)
            file.write(h2*2)
        file.write(h1)
    if filename!='gamesolution.txt': print(__file__.replace("file_operations.py",filename))      
    file.close()
