#6:15

import sys
from collections import deque
import copy
input=sys.stdin.readline

dx=[-1,1,0,0]
dy=[0,0,1,-1]


def play(R,N):
    new_map=[[0]*N for _ in range(N)]
    K=int(N/R)
    for i in range(K):
        for j in range(K):
            for i1 in range(R):
                for j1 in range(R):
                    new_map[R*i+i1][R*j+j1]=maps[R*i+(R-1)-j1][R*j+i1]

    chek_map=[]
    check_map=copy.deepcopy(new_map)
    for i in range(N):
        for j in range(N):
            x=i
            y=j
            count=0
            for w in range(4):
                nx=x+dx[w]
                ny=y+dy[w]
                if nx<0 or ny<0 or nx>=N or ny>=N:
                    continue
                if new_map[nx][ny]>0:
                    count+=1
            if count<3 and new_map[x][y]>0:
                check_map[x][y]-=1

    return check_map

def size_check():
    q=deque()
    result=0
    count=0
    check_map=[[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            mini_re=0
            count+=1
            if check_map[i][j]==0:
                q.append((i,j))
                while q:
                    x,y=q.popleft()
                    for w in range(4):
                        nx=x+dx[w]
                        ny=y+dy[w]
                        if nx<0 or ny<0 or nx>=N or ny>=N:
                            continue
                        if check_map[nx][ny]!=0 or maps[nx][ny]==0:
                            continue
                        q.append((nx,ny))
                        check_map[nx][ny]=count
                        mini_re+=1
            if mini_re>result:
                result=mini_re
    return result




N,Q=map(int,input().split())
size=1
for _ in range(N):
    size*=2
N=size
check_map=[[0]*N for _ in range(N)]

maps=[list(map(int,input().split())) for _ in range(size)]

L=list(map(int,input().split()))
for K1 in L:
    size=1
    for _ in range(K1):
        size*=2
    maps=play(size,N)


result1=0

for i in range(N):
    for j in range(N):
        result1+=maps[i][j]

print(result1)
result2=size_check()  

print(result2)
