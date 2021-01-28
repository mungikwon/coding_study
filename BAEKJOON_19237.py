import sys
from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]

input=sys.stdin.readline
import copy

N,M,K=map(int,input().split())
shark_lo=[[] for _ in range(M)]
time=[[0]*N for _ in range(N)]
smell=[]

shark_fi=[[[] for _ in range(4)] for _ in range(M)]


for i in range(N):
    line=list(map(int,input().split()))
    for j in range(len(line)):
        if line[j]!=0:
            shark_lo[line[j]-1].append((i,j))
            time[i][j]=K
    smell.append(line)

shark_dir=list(map(int,input().split()))

for w in range(M):
    shark_dir[w]=shark_dir[w]-1


for i in range(N):
    for j in range(N):
        smell[i][j]=smell[i][j]-1

for i in range(M):
    for j in range(4):
        shark_fi[i][j]=list(map(int,input().split()))
        for k in range(len(shark_fi[i][j])):
            shark_fi[i][j][k]=shark_fi[i][j][k]-1

def nextto():
    for i in range(N):
        for j in range(N):
            if time[i][j]!=0:
                time[i][j]=time[i][j]-1
            if time[i][j]==0:
                smell[i][j]=-1


w_t=1000
result=-1
while(w_t):
    w_t-=1

    r_t=0
    
    c_s=copy.deepcopy(smell)

    for i in range(M):
        [(x,y)]=shark_lo[i]
        z=shark_dir[i]
        if x==-1 and y==-1 and z==-1:
            r_t+=1
            if r_t==M-1:
                result=1000-w_t-1
                w_t=0
                break
            continue

        
        cp=0
        cp2=0

        for w in shark_fi[i][z]:
            nx=x+dx[w]
            ny=y+dy[w]

            if  nx<0 or ny<0 or nx>=N or ny>=N:
                continue
            if smell[nx][ny]!=-1 and time[nx][ny]==K+1 and c_s[nx][ny]==-1:
                shark_lo[i]=[(-1,-1)]
                shark_dir[i]=-1
                cp=1
                cp2=1
                break

            if smell[nx][ny]==-1:
                shark_lo[i]=[(nx,ny)]
                shark_dir[i]=w
                cp=1
                break
            
        if cp==1 and cp2==0:
            smell[nx][ny]=i
            time[nx][ny]=K+1

        if cp==0:
            for w in shark_fi[i][z]:
                nx=x+dx[w]
                ny=y+dy[w]
                if  nx<0 or ny<0 or nx>=N or ny>=N:
                    continue
                if smell[nx][ny]==i:
                    shark_lo[i]=[(nx,ny)]
                    shark_dir[i]=w
                    smell[nx][ny]=i
                    time[nx][ny]=K+1
                    break
    nextto()




    
print(result)


