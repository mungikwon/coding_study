import collections


N=int(input())
maplist=[[] for _ in range(N)]
dx=[-1,0,1,0]
dy=[0,-1,0,1]
result_list=[]

def bfs(kkk):
    for i in range(N):
        for j in range(N):
            if maplist[i][j]==1:
                q=collections.deque()
                q.append([i,j])
                maplist[i][j]=0
                result=1
                while q:
                    y,x=q.popleft()
                    for z in range(4):
                        nx,ny=x+dx[z],y+dy[z] 
                        if nx<0 or ny<0 or nx>=N or ny>=N:
                            continue
                        if maplist[ny][nx]==0:
                            continue
                        q.append([ny,nx])
                        maplist[ny][nx]=0
                        result+=1
                result_list.append(result)


for i in range(N):
    maplist[i]=list(map(int,input()))

bfs(maplist)
result_list.sort()
print(len(result_list))
for i in result_list:
    print(i)



