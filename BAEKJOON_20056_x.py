
#03:10

from collections import deque
import sys
input = sys.stdin.readline

N,M,K=map(int,input().split())

speed=[[0]*N for _ in range(N)]
mass=[[0]*N for _ in range(N)]
direction=[[0]*N for _ in range(N)]
count=[[0]*N for _ in range(N)]


q=deque()
map_info=deque()

dx=[-1,-1,0,1,1,1,0,-1]
dy=[0,1,1,1,0,-1,-1,-1]



for _ in range(M):
    r,c,m,s,d=map(int,input().split())
    q.append((r-1,c-1,m,s,d))

for _ in range(K+1):
    map_info=[]
    speed=[[0]*N for _ in range(N)]
    mass=[[0]*N for _ in range(N)]
    direction=[[0]*N for _ in range(N)]
    count=[[0]*N for _ in range(N)]
    direction_index=1
    di_key={}
    for _ in range(len(q)):
        
        r,c,m,s,d=q.popleft()
        newx=(r+dx[d]*s)%N
        newy=(c+dy[d]*s)%N
        mass[newx][newy]+=m
        speed[newx][newy]+=s
        
        if direction[newx][newy]==0:
            direction[newx][newy]=d
            di_key[newx,newy]=1
        elif direction[newx][newy]!=0:
            if direction[newx][newy]%2!=d%2:
                di_key[newx,newy]=-1
        count[newx][newy]+=1

        map_info.append((newx,newy))
    map_info=list(set(map_info))


    for x,y in map_info:
        if count[x][y]==1:
            q.append((x,y,mass[x][y],speed[x][y],direction[x][y]))

        if count[x][y]>=2:
            new_mass=mass[x][y]//5
            new_speed=speed[x][y]//count[x][y]
            if new_mass==0:
                continue

            if di_key[x,y]==1:
                for i in range(0,6+1,2):
                    q.append((x,y,new_mass,new_speed,i))
            elif di_key[x,y]==-1:
                for i in range(1,8,2):
                    q.append((x,y,new_mass,new_speed,i))


result=0
for i in range(N):
    for j in range(N):
        if mass[i][j]!=0:
            result+=mass[i][j]
print(result)





