""" import collections

N=int(input())
N_list=[[] for _ in range(N+1)]
result=0
result_list=[]


def bfs(N_list,i):
    visited=[1]*(N+1)
    q=collections.deque()
    q.append(N_list[i][0])
    visited[i]=0
    
    while q:
        k=q.popleft()
        if visited[k] or ==0:
            continue
        q.append(N_list[k][0])
        result_list.append(k)
        print("result_list")
    return result_list


for i in range(1,N+1):
    N_list[i].append(int(input()))



for i in range(1,N+1):
    a=bfs(N_list,i)
    print(a)

 """