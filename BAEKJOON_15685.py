

dx=[1,0,-1,0]
dy=[0,-1,0,1]


import sys

input=sys.stdin.readline

N=int(input())
maps=[[0]*101 for _ in range(101)]
for _ in range(N):
    dir=[]
    x,y,d,g=map(int,input().split())
    maps[x][y]=1

    dir.append(d)
    for _ in range(g):
        dir2=[]
        for k in range(len(dir)-1,-1,-1):
            dir2.append((dir[k]+1)%4)
        dir=dir+dir2


    for d in dir:
        x=x+dx[d]
        y=y+dy[d]
        if x<0 or y<0 or x>100 or y>100:
            continue
        maps[x][y]=1
        

result=0
for i in range(100):
    for j in range(100):
        if maps[i][j]==1 and maps[i+1][j]==1 and maps[i][j+1]==1 and maps[i+1][j+1]==1:
            result+=1

print(result)
