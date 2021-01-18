#1025

import sys
from collections import deque
import copy
input=sys.stdin.readline

dx=[-1,1,0,0]
dy=[0,0,1,-1]


def rotate(xi,di,k):
    change_map=copy.deepcopy(maps)
    for i in range(xi-1,N,xi):
        if di==0:
            for j in range(M):
                maps[i][j]=change_map[i][(j-k)%M]
        if di==1:
            for j in range(M):
                maps[i][j]=change_map[i][(j+k)%M]


def check():
    q=deque()
    check_maps=[[-1]*M for _ in range(N)]
    for x1 in range(N):
        for y1 in range(M):
            if maps[x1][y1]!=0 and check_maps[x1][y1]!=0:
                q.append((x1,y1))
            while q:
                x,y=q.popleft()
                for i in range(4):
                    nx=x+dx[i]
                    ny=y+dy[i]
                    ny=ny%M
                    if nx<0 or nx>=N:
                        continue
                    if maps[x][y]==0 or check_maps[nx][ny]==0:
                        continue
                    if maps[x][y]==maps[nx][ny]:
                        if check_maps[x][y]==-1:
                            check_maps[x][y]=0
                        check_maps[nx][ny]=0
                        q.append((nx,ny))
    ch=0
    sums=0
    for i in range(N):
        for j in range(M):
            if check_maps[i][j]==0:
                maps[i][j]=0
                ch=1


    check_maps=[[0]*M for _ in range(N)]
    if ch==0:
        for i in range(N):
            for j in range(M):
                if maps[i][j]!=0:
                    sums+=maps[i][j]
                    ch+=1
        if ch>0:
            avr=sums/ch
        if ch==0:
            avr=0
    
        for i in range(N):
            for j in range(M):
                if maps[i][j]!=0:
                    if maps[i][j]>avr:
                        check_maps[i][j]=-1
                    elif maps[i][j]<avr:
                        check_maps[i][j]=+1
        for i in range(N):
                for j in range(M):
                    maps[i][j]+=check_maps[i][j]


N,M,T = map(int,input().split())
maps=[]
for i in range(N):
    maps.append(list(map(int,input().split())))


for _ in range(T):
    xi,di,ki = map(int,input().split())
    rotate(xi,di,ki)
    check()
 


result=0
for i in range(N):
    for j in range(M):
        result+=maps[i][j]
print(result)

