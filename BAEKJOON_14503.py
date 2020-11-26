from collections import deque


N,M = map(int,input().split())
r,c,d=map(int,input().split())
maps=[list(map(int,input().split())) for _ in range(N)]

dx=[-1,0,1,0]
dy=[0,1,0,-1]




def search(r,c,d):
    check=0
    while(1):
        d=(d-1)%4
        if maps[r+dx[d]][c+dy[d]]==0:
            return ((r+dx[d],c+dy[d],d))
        if maps[r+dx[d]][c+dy[d]]!=0:
            check+=1
        if check==4:
            lo=(d-2)%4
            if maps[r+dx[lo]][c+dy[lo]]==1:
                return (-1,-1,-1)
            else:
                check=0
                r=r+dx[lo]
                c=c+dy[lo]

while(1):
    maps[r][c]=2
    r,c,d=search(r,c,d)
    if r==-1:
        break
    
result=0
for i in range(N):
    for j in range(M):
        if maps[i][j]==2:
            result+=1

print(result)