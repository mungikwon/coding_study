import sys

input=sys.stdin.readline

r,c,k = map(int,input().split())

maps=[list(map(int,input().split())) for _ in range(3)]



def sort_line(line): #라인에 맞게 쏠트함. 다만 현재크기보다 작을테니..
    result=[]
    sort_line=[0]*(max(line)+1)
    line.sort()

    for i in range(len(line)):
        sort_line[line[i]]+=1

    count=1
    for i in range(1,max(sort_line)+1):
        for j in range(1,len(sort_line)):
            if sort_line[j]==count:
                result.append(j)
                result.append(count)
        count+=1
    return result


go=0
while(1):
    R=len(maps)
    L=len(maps[0])
    if r<=R and c<=L: 
        if maps[r-1][c-1]==k:
            break

    new_map=[]
    if R>=L:
        count=0
        for i in range(R):
            new_line=sort_line(maps[i])
            if len(new_line)>count:
                count=len(new_line)
                
            new_map.append(new_line)
        for i in range(R):
            for _ in range(count-len(new_map[i])):
                new_map[i].append(0)
        maps=new_map    
    
    elif L>R:
        count=0
        for i in range(L):
            l=[]
            for w in range(R):
                l.append(maps[w][i])
            new_line=sort_line(l)
            if len(new_line)>count:
                count=len(new_line)
            new_map.append(new_line)

        for i in range(len(new_map)):
            for _ in range(count-len(new_map[i])):
                new_map[i].append(0)


        maps=[[0]*L for _ in range(count)]

        for i in range(count):
            for j in range(L):
                maps[i][j]=new_map[j][i]
    maps=maps[:100][:100]
    go+=1
    if go==101:
        go=-1
        break

print(go)

