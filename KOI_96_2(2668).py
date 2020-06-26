import collections

N=int(input())
N_list=[[] for _ in range(N+1)]
result=0
result_final=[]

def bfs(N_list,i):
    visited=[1]*(N+1)
    result_list=[]
    test_list=[]
    q=collections.deque()
    q.append(N_list[i][0])
    result_list.append(i)
    visited[i]=0    
    while q:
        k=q.popleft()
        if visited[k]==0:
            break
        q.append(N_list[k][0])
        visited[k]=0   
        result_list.append(k)
    for z in result_list:
        test_list.append(N_list[z][0])

    result_list.sort()
    test_list.sort()
    print(result_list)
    print(test_list)
    print(len(result_list))
    for i in range(len(result_list)):
        print(i)
        print("r",result_list[i])
        print("t",test_list[i])
        if result_list[i]!=test_list[i]:
            result_list=[]
    return result_list

for i in range(1,N+1):
    N_list[i].append(int(input()))
    if N_list[i][0]==i:
        result_final.append(i)


for i in range(1,N+1):
    a=bfs(N_list,i)

    if len(a)>result:
        result_final=a+result_final
        result=len(result_final)

    
print(result)
result_final.sort()
for i in result_final:
    print(i)


