
import sys
from collections import deque

input=sys.stdin.readline
maps=[]
N,M,R=map(int,input().split())
s_maps=[[0]*N for _ in range(N)]
d_maps=[[[] for _ in range(N)] for _ in range(N)]

dx=[-1,1,0,0]
dy=[0,0,1,-1]





def find_st(x,y):
    if s_maps[x][y]!=0:
        return x,y,0,s_maps[x][y]
    check_map=[[-1]*N for _ in range(N)]
    check_map[x][y]=0
    q=deque()
    q.append((x,y))
    ex=[]
    ns=9999
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>=N or ny>=N:
                continue
            if maps[nx][ny]==1:    
                continue
            if check_map[nx][ny]!=-1:
                continue
            q.append((nx,ny))
            check_map[nx][ny]=check_map[x][y]+1
            if s_maps[nx][ny]!=0:
                if ns>check_map[nx][ny]:
                    ns=check_map[nx][ny]
                if ns==check_map[nx][ny]:
                    ex.append((nx,ny))

    if ex:
        ex.sort()
        nx,ny=ex[0]
        return nx,ny,check_map[nx][ny],s_maps[nx][ny]

    for i in range(N):
        for j in range(N):
            if check_map[i][j]==-1 and s_maps[i][j]!=0:
                return -1,-1,-1,-1
                

def find_de(x,y,n):
    check_map=[[-1]*N for _ in range(N)]
    check_map[x][y]=0
    q=deque()
    q.append((x,y))
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>=N or ny>=N:
                continue
            if maps[nx][ny]==1:
                continue

            if check_map[nx][ny]!=-1:
                continue
            q.append((nx,ny))
            check_map[nx][ny]=check_map[x][y]+1
            if d_maps[nx][ny]:
                for w1 in d_maps[nx][ny]:
                    if w1==n:
                        return nx,ny,check_map[nx][ny]
    

    return -1,-1,-1

for _ in range(N):
    line=list(map(int,input().split())) 
    maps.append(line)

x,y=map(int,input().split())
x=x-1
y=y-1

for i in range(M):
    x1,y1,lox,loy=map(int,input().split())
    s_maps[x1-1][y1-1]=i+1
    d_maps[lox-1][loy-1].append(i+1)


for _ in range(M):
    x,y,o,n=find_st(x,y)
    s_maps[x][y]=0
    
    if x==-1:
        R=-1
        break
    R=R-o
    if R<0:
        R=-1
        break

    x,y,o=find_de(x,y,n)
    if x==-1:
        R=-1
        break
    R=R-o
    if R<0:
        R=-1
        break
    R=R+o*2


print(R)