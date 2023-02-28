def read():
    grid=[]
    file=open('out.txt', 'r')
    for line in file:
        if '-' in line:break
    lst=[-1]*9
    for l in file: 
        line=l.replace('||','|').replace(' ','').strip()[1:-1].split('|')
    
        if '-' in line[0]:
            if -1 in lst:
                return "unfound value "
            grid.append(lst);lst=[-1]*9
            if len(grid)%3==0:file.readline()
            continue
        
        for idx, unti in enumerate(line):
            u=unti.strip()
            if  u=='' :    continue
            if not u.isdigit():
                return "value not a number"
            lst[idx]=int(u)
    return grid 