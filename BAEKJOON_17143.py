import sys
from collections import deque


dx=[-1,1,0,0]
dy=[0,0,1,-1]

input=sys.stdin.readline

R,C,M=map(int,input().split())


maps=[[0]*C for _ in range(R)]

shark=deque()

for i in range(M):
    r,c,s,d,z=map(int,input().split())
    maps[r-1][c-1]=[z,s,d-1]
    shark.append((r-1,c-1))


def fishing(a):
    r=0
    for i in range(R):
        if maps[i][a]!=0:
            r=maps[i][a][0]
            maps[i][a]=0
            break
    return r



def move(maps):
    new_maps=[[0]*C for _ in range(R)]
    for _ in range(len(shark)):
        i,j=shark.popleft()
        if maps[i][j]==0:
            continue

        z,s,d=maps[i][j]
        if d==0 or d==1:
            s1=s
            nx=i
            ny=j
            while(1):
                if s1==0:
                    break
                if nx==0 and d==0:
                    d=(d+1)%2
                elif nx==R-1 and d==1:
                    d=(d+1)%2
                nx=nx+dx[d]
                s1=s1-1

        if d==2 or d==3:
            nx=i
            ny=j
            s1=s
            while(1):
                if s1==0:
                    break
                if d==2 and ny==C-1:
                    d=d+1
                elif d==3 and ny==0:
                    d=d-1
                ny=ny+dy[d]
                s1=s1-1
        maps[i][j]=0
        if new_maps[nx][ny]!=0:
            if new_maps[nx][ny][0]>z:
                continue
        shark.append((nx,ny))
        new_maps[nx][ny]=[z,s,d]
    return new_maps        



king=-1
result=0
while(king<C-1):
    if M==0:
        break
    king=king+1
    result+=fishing(king)
    maps=move(maps)

print(result)




