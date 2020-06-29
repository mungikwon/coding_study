import collections

N=int(input())
room_list=[]
room_list.append((0,0))
result=[]

def bfs(k):
    visited=[0]*(N+1)
    q=collections.deque()
    q.append(room_list[k][1])
    visited[k]=1
    while q:
        a=q.popleft()
        if visited[a]==1:
            continue
        visited[a]=1
        q.append(room_list[a][1])
    sum1=[]
    sum2=[]
    for i in range(len(room_list)):
        if visited[i]==1:
            sum1.append(i)
            sum2.append(room_list[i][1])
    sum1.sort()
    sum2.sort()
    for i in range(len(sum1)):
        if sum1[i]!=sum2[i]:
            return []
    return k
            

for i in range(1,N+1):
    a=int(input())
    room_list.append((i,a))

for k in range(1,N+1):
    a=bfs(k)
    if a:
        result.append(a)

print(len(result))
for i in result:
    print(i)