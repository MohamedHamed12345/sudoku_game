def read_extract():
    file=open('solution.txt','r',encoding='utf-8',errors='ignore')
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
    print(board)
    return board


    