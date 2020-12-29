import sys
from collections import deque

input=sys.stdin.readline

N=int(input())
shark=deque()
maps=[]
result=0
shark_size =2
shark_ex=0


dx=[-1,0,0,1]
dy=[0,-1,1,0]

def bfs(i,j):
    global shark_size,shark_ex,result
    check_map=[[-1]*N for _ in range(N)]
    q=deque()
    q.append((i,j))
    check_map[i][j]=0
    check=9999
    check_list=[]

    while q:
        x,y=q.popleft()
        for w in range(4):
            nx=x+dx[w]
            ny=y+dy[w]
            if nx<0 or ny<0 or nx>=N or ny>=N:
                continue
            if check_map[nx][ny]!=-1 or maps[nx][ny]>shark_size:
                continue
            check_map[nx][ny]=check_map[x][y]+1
            q.append((nx,ny))
            if maps[nx][ny]!=0 and maps[nx][ny]<shark_size:                
                if check_map[nx][ny]<check:
                    check=check_map[nx][ny]
                if check_map[nx][ny]!=check:
                    break
                check_list.append((nx,ny))
    if check_list:
        check_list.sort()
        nx,ny=check_list[0]
        shark_ex+=1
        maps[i][j]=0
        shark.append((nx,ny))
        result+=check_map[nx][ny]
        return False

    return True


            

    

for i in range(N):
    line=list(map(int,input().split()))
    for j in range(len(line)):
        if line[j]==9 :
            shark.append((i,j))
    maps.append(line)

while(1):
    i,j=shark.popleft()
    maps[i][j]=9
    if bfs(i,j)==True:
        break
    if shark_ex==shark_size:
        shark_ex=0
        shark_size+=1

print(result)


