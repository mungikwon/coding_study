from itertools import combinations
from collections import deque

N,M = map(int,input().split())
maps=[]
home=[]
chicken=[]
result=1e9

dx=[-1,1,0,0]
dy=[0,0,-1,1]


for i in range(N):
    line=list(map(int,input().split()))
    for j in range(N):
        if line[j]==1:
            home.append((i,j))
        if line[j]==2:
            chicken.append((i,j))
    maps.append(line)




chicken_list=combinations(chicken,M)
chicken_list=list(chicken_list)



for last_ck in chicken_list:
    mini_result=0
    for each_home in home:
        num=10e8
        for ck in last_ck:
            if num>(abs(ck[0]-each_home[0])+abs(ck[1]-each_home[1])):
                num=(abs(ck[0]-each_home[0])+abs(ck[1]-each_home[1]))
        mini_result+=num
            
    if result>mini_result:
        result=mini_result



print(result)