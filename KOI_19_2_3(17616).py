# -*- coding: utf-8 -*-
"""
Created on Mon May 18 14:43:39 2020

@author: USER
"""
from collections import deque

N,M,X = map(int,input().split())
lower=[[] for _ in range(N+1)]
higher=[[] for _ in range(N+1)]


def bfs(X,what):
    visited=[0]*(N+1)
    result=0
    q=deque()
    q.append(X)
    visited[X]=1
    
    while q:
        v=q.popleft()
        for i in what[v]:
            if visited[i]==0:
                q.append(i)
                visited[i]=1
                result+=1
    return result
                
    
    
    
    

for _ in range(M):
    A,B= map(int,input().split())
    lower[B].append(A)
    higher[A].append(B)
    
print(1+bfs(X,lower),N-bfs(X,higher))
    
