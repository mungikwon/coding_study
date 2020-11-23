from collections import deque

def bfs(x):
    q=deque()
    q.append(x)
    while q:
        l=q.popleft()
        for i in maps[l]:
            q.append(i)
            if result[i]==-1:
                result[i]=result[l]+1



N,M,K,X = map(int,input().split())
maps=[[] for _ in range(N+1)]
for _ in range(M):
    c,r=map(int,input().split())
    maps[c].append(r)
result=[-1]*(N+1)


result[X]=0
bfs(X)


check=False
for w in range(1,N+1):
    if result[w]==K:
        print(w)
        check=True

if check==False:
    print(-1)
