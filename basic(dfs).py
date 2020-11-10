
def dfs(x,y):
    if x<0 or x>=N or y<0 or y>=M or maps[x][y]==1:
        return
    if maps[x][y]==0:
        maps[x][y]=1
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)


N,M = map(int,input().split())
maps=[list(map(int,input())) for _ in range(N)]
result=0

for i in range(N):
    for j in range(M):
        if maps[i][j]==0:
            dfs(i,j)
            result+=1

        

print(result)
