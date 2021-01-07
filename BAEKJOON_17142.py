import sys
from collections import deque
from itertools import combinations 

input=sys.stdin.readline
N,M=map(int,input().split())
dx=[-1,1,0,0]
dy=[0,0,1,-1]
maps=[]
virus=[]
result=N*N

def bfs(a):
    q=deque()
    check_maps=[[-1]*N for _ in range(N)]
    r=0

    for x,y in a:
        check_maps[x][y]=0
        q.append((x,y))
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>=N or ny>=N:
                continue
            if check_maps[nx][ny]!=-1 or maps[nx][ny]==1:
                continue
            check_maps[nx][ny]=check_maps[x][y]+1
            q.append((nx,ny))

    for x,y in virus:
        check_maps[x][y]=0
        q.append((x,y))

    for i in range(N):
        for j in range(N):
            if maps[i][j]!=1 and check_maps[i][j]==-1:
                return N*N
            if check_maps[i][j]>r:
                r=check_maps[i][j]
    return r
    

for i in range(N):
    line=list(map(int,input().split()))
    maps.append(line)
    for j in range(N):
        if line[j]==2:
            virus.append((i,j))


virus_list=list(combinations(virus,M))

for i in virus_list:
    R=bfs(i)
    if result>R:
        result=R 

if result==N*N:
    result=-1
print(result)

