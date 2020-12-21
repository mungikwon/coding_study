import sys
from itertools import combinations


a=combinations([1,2,3],0)


input=sys.stdin.readline

N,M,H = map(int,input().split())


maps=[[0]*N for _ in range(H)]
ex_list=[]

for i in range(H):
    for j in range(N):
        ex_list.append((i,j))

for _ in range(M):
    a,b=map(int,input().split())

    maps[a-1][b-1]=1
    ex_list.remove((a-1,b-1))
    if b<N:
        ex_list.remove((a-1,b))

def map_check():
 
    for i in range(H):
        for j in range(N-1):
            if maps[i][j]==1 and maps[i][j+1]==1:
                return False
    return True
            

def check():
    for i in range(N):
        x=0
        y=i
        while(x<H):
            if y!=0 and maps[x][y-1]==1:
                y-=1
            elif y!=(N-1) and maps[x][y]==1:
                y+=1
            x+=1
        if i != y:
            return False
    return True

def play():
    if map_check()==False:
        return -1
    if check()==True:
        return 0

    for i in range(1,4):
        coms=combinations(ex_list,i)
        for com in coms:
            for x,y in com:
             
                maps[x][y]=1

            if map_check()==True:
                if check()==True:
                    return i
            for x,y in com:
                maps[x][y]=0
    return -1

print(play())