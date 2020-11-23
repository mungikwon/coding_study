from collections import deque

N,M,K,X=map(int,input().split())
maps=[[] for _ in range(N)]
distance=[-1]*N
result=[]


def bfs(X):
    q=deque()
    q.append(X)
    while q:
        go=q.popleft()
        for w in maps[go]:
            if distance[w]==-1:
                distance[w]=distance[go]+1
                q.append(w)

        
    

for _ in range(M):
    A,B=map(int,input().split())
    maps[A-1].append(B-1)

distance[X-1]=0


bfs(X-1)
for i in range(len(distance)):
    if distance[i]==K:
        result.append(i+1)

result.sort()

if result:
    for k in result:
        print(k)
else:
    print(-1)