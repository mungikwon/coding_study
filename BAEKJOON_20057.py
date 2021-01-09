#4:15
import sys

dx=[0,1,0,-1]
dy=[-1,0,1,0]



direction_n=[]

def make_direction_n():
    a=1
    count=0
    while(1):
        direction_n.append(a)
        count+=1
        if count%2==0:
            a+=1
        if sum(direction_n)>=(N*N-1):
            break
    direction_n[-1]=direction_n[-1]-(sum(direction_n)-(N*N-1))

def play(x,y,d):
    alpa=A[x][y]    
    nx=x+2*dx[d]
    ny=y+2*dy[d]

    if nx>=0 and ny>=0 and nx<N and ny<N:
        A[nx][ny]+=int(A[x][y]*0.05)
    alpa-=int(A[x][y]*0.05)
    
    nx=x+2*dx[(d+3)%4]
    ny=y+2*dy[(d+3)%4]    
    if nx>=0 and ny>=0 and nx<N and ny<N:
        A[nx][ny]+=int(A[x][y]*0.02)
    alpa-=int(A[x][y]*0.02)

    nx=x+dx[(d+3)%4]
    ny=y+dy[(d+3)%4]    
    if nx>=0 and ny>=0 and nx<N and ny<N:
        A[nx][ny]+=int(A[x][y]*0.07)
    alpa-=int(A[x][y]*0.07)

    nx=x+2*dx[(d+1)%4]
    ny=y+2*dy[(d+1)%4]    
    if nx>=0 and ny>=0 and nx<N and ny<N:
        A[nx][ny]+=int(A[x][y]*0.02)
    alpa-=int(A[x][y]*0.02)    

    nx=x+dx[(d+1)%4]
    ny=y+dy[(d+1)%4]    
    if nx>=0 and ny>=0 and nx<N and ny<N:
        A[nx][ny]+=int(A[x][y]*0.07)
    alpa-=int(A[x][y]*0.07)


    nx=x+dx[(d+1)%4]+dx[d]
    ny=y+dy[(d+1)%4]+dy[d]    
    if nx>=0 and ny>=0 and nx<N and ny<N:
        A[nx][ny]+=int(A[x][y]*0.1)
    alpa-=int(A[x][y]*0.1)

    nx=x+dx[(d+3)%4]+dx[d]
    ny=y+dy[(d+3)%4]+dy[d]    
    if nx>=0 and ny>=0 and nx<N and ny<N:
        A[nx][ny]+=int(A[x][y]*0.1)
    alpa-=int(A[x][y]*0.1)

    nx=x+dx[(d+3)%4]+dx[(d+2)%4]
    ny=y+dy[(d+3)%4]+dy[(d+2)%4]    
    if nx>=0 and ny>=0 and nx<N and ny<N:
        A[nx][ny]+=int(A[x][y]*0.01)
    alpa-=int(A[x][y]*0.01)

    nx=x+dx[(d+1)%4]+dx[(d+2)%4]
    ny=y+dy[(d+1)%4]+dy[(d+2)%4]    
    if nx>=0 and ny>=0 and nx<N and ny<N:
        A[nx][ny]+=int(A[x][y]*0.01)
    alpa-=int(A[x][y]*0.01)
    
    nx=x+dx[d]
    ny=y+dy[d]
    if nx>=0 and ny>=0 and nx<N and ny<N:
        A[nx][ny]+=alpa
    A[x][y]=0


input=sys.stdin.readline
N=int(input())
A=[list(map(int,input().split())) for _ in range(N)]


make_direction_n()


d=0
x=N//2
y=N//2

result=0
for i in range(N):
    for j in range(N):
        result+=A[i][j]

for di in direction_n:
    for _ in range(di):
        x=x+dx[d%4]
        y=y+dy[d%4]
        play(x,y,d%4)
    d+=1


for i in range(N):
    for j in range(N):
        result-=A[i][j]

print(result)
    

