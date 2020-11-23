from collections import deque


def bfs(x,y):
    q=deque()
    q.append((x,y))
    while(q):
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=N or ny<0 or ny>=M:
                continue
            if maps[nx][ny]==1:
                continue
            else:
                q.append((nx,ny))
                maps[nx][ny]=1


N,M = map(int,input().split())

maps=[list(map(int,input())) for _ in range(N)]

result=0
dx=[-1,1,0,0]
dy=[0,0,-1,1]


for i in range(N):
    for j in range(M):
        if maps[i][j]==0:
            maps[i][j]=1
            bfs(i,j)
            result+=1

print(result)               