from collections import deque

N,M,K=map(int,input().split())
q=deque()
dx=[-1,-1,0,1,1,1,0,-1]
dy=[0,1,1,1,0,-1,-1,-1]

for _ in range(M):
    q.append((list(map(int,input().split()))))

for _ in range(K+1):
    mapsm=[[0]*N for _ in range(N)]
    mapss=[[0]*N for _ in range(N)]
    mapsd=[[0]*N for _ in range(N)]
    mapsc=[[0]*N for _ in range(N)]
    mapsd_ch=[[0]*N for _ in range(N)]


    for _ in range(len(q)):
        r,c,m,s,d=q.popleft()
        mapsm[(r+dx[d]*s)%N][(c+dy[d]*s)%N]+=m
        mapss[(r+dx[d]*s)%N][(c+dy[d]*s)%N]+=s
        if mapsc[(r+dx[d]*s)%N][(c+dy[d]*s)%N]==0:
            mapsd_ch[(r+dx[d]*s)%N][(c+dy[d]*s)%N]=d
        if mapsc[(r+dx[d]*s)%N][(c+dy[d]*s)%N]!=0:
            if mapsd_ch[(r+dx[d]*s)%N][(c+dy[d]*s)%N]%2!=d%2:
                mapsd[(r+dx[d]*s)%N][(c+dy[d]*s)%N]=1
        mapsc[(r+dx[d]*s)%N][(c+dy[d]*s)%N]+=1

    for i in range(N):
        for j in range(N):
            if mapsc[i][j]==1:
                q.append((i,j,mapsm[i][j],mapss[i][j],mapsd_ch[i][j]))
            if mapsc[i][j]>1:
                if mapsm[i][j]//5>0:
                    if mapsd[i][j]==0:
                        for dd in range(0,7,2):
                            q.append((i,j,mapsm[i][j]//5,mapss[i][j]//mapsc[i][j],dd))
                    if mapsd[i][j]==1:
                        for dd in range(1,8,2):
                            q.append((i,j,mapsm[i][j]//5,mapss[i][j]//mapsc[i][j],dd))
result=0
for i in range(N):
    for j in range(N):
        result+=mapsm[i][j]

print(result)


    