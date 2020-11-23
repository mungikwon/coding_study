from collections import deque
from itertools import combinations
import copy

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def find_empty():
    for i in range(N):
        for j in range(M):
            if maps[i][j]==0:
                empty.append((i,j))
def bfs(x,y):
    q=deque()
    q.append((x,y))
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=N or ny<0 or ny>=M:
                continue
            if new_maps[nx][ny]!=0:
                continue
            q.append((nx,ny))
            new_maps[nx][ny]=2
        





final_result=0
empty=[]
N,M=map(int,input().split())

maps=[list(map(int,input().split())) for _ in range(N)]

find_empty()
hall_ex=list(combinations(empty,3))


for halls in hall_ex:
    new_maps=copy.deepcopy(maps)
    result=0
    for e_hall in halls:
        new_maps[e_hall[0]][e_hall[1]]=1
    for i in range(N):
        for j in range(M):
            if new_maps[i][j]==2:
                bfs(i,j)
    for i in range(N):
        for j in range(M):
            if new_maps[i][j]==0:
                result+=1
    if result>final_result:
        final_result=result

print(final_result)