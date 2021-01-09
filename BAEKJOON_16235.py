import sys 
from collections import deque

input=sys.stdin.readline
N,M,K=map(int,input().split())

en=[[5]*N for _ in range(N)]
A=[]
tree=[[deque() for _ in range(N)] for _ in range(N)]

for _ in range(N):
    A.append(list(map(int,input().split())))

for _ in range(M):
    x,y,z=map(int,input().split())
    tree[x-1][y-1].append(z)

for _ in range(K):
    for i in range(N):
        for j in range(N):
            mini_tree=[]
            ens=0
            if tree[i][j]:
                while tree[i][j]:
                    t=tree[i][j].popleft()
                    mini_tree.append(t)
                mini_tree.sort()
                for w in range(len(mini_tree)):
                    if en[i][j]>=mini_tree[w]:
                        en[i][j]-=mini_tree[w]
                        tree[i][j].append(mini_tree[w]+1)
                    else:
                        ens+=mini_tree[w]//2
            en[i][j]+=ens
    

    for i in range(N):
        for j in range(N):
            if tree[i][j]:
                mini_tree=list(tree[i][j])
                for w in range(len(mini_tree)):
                    if mini_tree[w]%5==0:
                        for w1 in range(-1,2,1):
                            for w2 in range(-1,2,1):
                                if w1==0 and w2==0:
                                    continue
                                x1=i+w1
                                y1=j+w2
                                if x1<0 or y1<0 or x1>=N or y1>=N:
                                    continue
                                tree[x1][y1].append(1)

    for i in range(N):
        for j in range(N):
            en[i][j]+=A[i][j]


    
result=0
for i in range(N):
    for j in range(N):
        if tree[i][j]:
            result+=len(tree[i][j])

    

print(result)