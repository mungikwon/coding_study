import sys
from collections import deque

input=sys.stdin.readline

N=int(input())

maps=[list(map(int,input().split())) for _ in range(N)]

dx=[0,0,-1,1]
dy=[-1,1,0,0]


def play(x,y,d1,d2):
    area=[0,0,0,0,0]
    check_map=[[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i<x+d1 and j<=y:
                check_map[i][j]=1
            if i<=x+d2 and j>y:
                check_map[i][j]=2
            if x+d1<=i and j<y-d1+d2:
                check_map[i][j]=3
            if x+d2<i and j>=y-d1+d2:
                check_map[i][j]=4
    for i1 in range(d1+1):
        check_map[x+i1][y-i1]=5
        check_map[x+d2+i1][y+d2-i1]=5
    for i1 in range(d2+1):
        check_map[x+i1][y+i1]=5
        check_map[x+d1+i1][y-d1+i1]=5
    
    q=deque()
    q.append((x+1,y))
    check_map[x+1][y]=5
    while q:
        xx,yy=q.popleft()
        for ii in range(4):
            nx=xx+dx[ii]
            ny=yy+dy[ii]
            if check_map[nx][ny]==5:
                continue
            q.append((nx,ny))
            check_map[nx][ny]=5
    q=deque()
    q.append((x+d1+d2-1,y-d1+d2))
    check_map[x+d1+d2-1][y-d1+d2]=5
    while q:
        xx,yy=q.popleft()
        for ii in range(4):
            nx=xx+dx[ii]
            ny=yy+dy[ii]
            if check_map[nx][ny]==5:
                continue
            q.append((nx,ny))
            check_map[nx][ny]=5

    for i in range(N):
        for j in range(N):
            for k in range(5):
                if check_map[i][j]==k+1:
                    area[k]+=maps[i][j]
    
    return max(area)-min(area)


result=9999999
for i in range(0,N):
    for j in range(0,N):
        for d1 in range(1,j+1):
            for d2 in range(1,N-j):
                if i+d1+d2>=N:
                    continue

                r=play(i,j,d1,d2)
                if r<result:
                    result=r



print(result)