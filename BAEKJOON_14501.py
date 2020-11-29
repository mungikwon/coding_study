N=int(input())
info=[]
result=0
for i in range(1,N+1):
    T,P=map(int,input().split())
    if i+T-1>N:
        continue
    search=0
    if info:
        for i1,j1 in info:
            if i1<i:
                if j1>search:
                    search=j1 
    if P+search>result:
        result=P+search
    info.append((i+T-1,P+search))
print(result)