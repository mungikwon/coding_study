from collections import deque
nx=[-1,1,0,0]
ny=[0,0,-1,1]

N,K=map(int,input().split())

maps=[list(map(int,input().split())) for _ in range(N)]

S,X,Y=map(int,input().split())

virus=[]

def spread(v_info,second):
    q=deque()
    for k in v_info:
       q.append(k)
    while q:
        x,y,n,s=q.popleft()
        if s>second:
            break
        for i in range(4):
            dx=x+nx[i]
            dy=y+ny[i]
            if dx<0 or dy<0 or dx>=N or dy>=N:
                continue
            if maps[dx][dy]==0:
                maps[dx][dy]=n
                q.append((dx,dy,n,s+1))





for i in range(N):
    for j in range(N):
        if maps[i][j]>0:
            virus.append((i,j,maps[i][j],1))
virus.sort(key=lambda x:x[2])

spread(virus,S)

print(maps[X-1][Y-1])

