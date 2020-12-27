from collections import deque

import sys

input=sys.stdin.readline

N,L,R=map(int,input().split())

maps=[list(map(int,input().split())) for _ in range(N)]

dx=[1,-1,0,0]
dy=[0,0,1,-1]


result=0
q=deque()

while(1):
    cal=[]

    check_map=[[0]*N for _ in range(N)]
    k=1
    for i in range(N):
        for j in range(N):
            if check_map[i][j]==0:
                p=0
                c=0
                check_map[i][j]=k
                q.append((i,j,k))
                while q:
                    x,y,k=q.popleft()
                    p+=maps[x][y]
                    c+=1

                    for w in range(4):
                        nx=x+dx[w]
                        ny=y+dy[w]
                        if nx<0 or ny<0 or nx>=N or ny>=N or check_map[nx][ny]!=0:
                            continue
                        if abs(maps[nx][ny]-maps[x][y])>=L and abs(maps[nx][ny]-maps[x][y])<=R:
                            q.append((nx,ny,k))
                            check_map[nx][ny]=k
                cal.append(p//c)
                k+=1


    if k==N*N+1:
        break
    
    for i in range(N):
        for j in range(N):
            maps[i][j]=cal[check_map[i][j]-1]

    result+=1

print(result)

