N=int(input())
point_info=[[] for i in range(N)]
result=0
check=[]

for i in range(N):
    a,b=map(int,input().split())
    point_info[b].append(a)
    check.append(b)

check=set(check)

for i in check:
    point_info[i].sort()
    print(point_info[i])
    print(point_info[i][1]-point_info[i][0]) 
    size=len(point_info[i])
    for k in range(1,len(point_info[i])-1):
        print(min(point_info[i][k]-point_info[i][k-1],point_info[i][k+1]-point_info[i][k]))
    print(point_info[i][size-1]-point_info[i][size-2])
print(result)