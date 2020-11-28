from collections import deque


N=int(input())
maps=[[0]*N for i in range(N)]
snake_info=deque()
snake=deque()

dx=[0,1,0,-1]
dy=[1,0,-1,0]


def play(x,y,d):
    nx=x+dx[d]
    ny=y+dy[d]
    if nx<0 or ny<0 or nx>=N or ny>=N or maps[nx][ny]==2:
        return -1,-1,-1
    if maps[nx][ny]==0:
        lx,ly=snake.popleft()
        maps[lx][ly]=0
    maps[nx][ny]=2
    snake.append((nx,ny))

    return nx,ny,d


K=int(input())
for _ in range(K):
    apple_x,apple_y=map(int,input().split())
    maps[apple_x-1][apple_y-1]=1


L=int(input())
for _ in range(L):
    X,C=input().split()
    snake_info.append((int(X),C))
snake_info.append((10001,'W'))


X,C=snake_info.popleft()
time=0
x=0
y=0
d=0
maps[x][y]=2
snake.append((x,y))
while(1):
    if time==X:
        if C=='L':
            d=(d-1)%4
        if C=='D':
            d=(d+1)%4
        X,C=snake_info.popleft()
    x,y,d=play(x,y,d)
    time+=1
    if x==-1:
        break

print(time)