from itertools import permutations,product
import copy


N,M=map(int,input().split())
map_info=[[] for _ in range(7)]
cctv_case=[]
maps=[]
di=[(0,1),(1,0),(0,-1),(-1,0)]

def directions(n,d):
    if n==1:
        return (di[d])      
    if n==2:
        return (di[d%2],di[d%2+2])
    if n==3:
        return (di[d%4],di[(d+1)%4])
    if n==4:
        return (di[d%4],di[(d+1)%4],di[(d+2)%4])
    if n==5:
        return (di[0],di[1],di[2],di[3])


def check(x,y,dx,dy):

    if x<0 or y<0 or x>=N or y>=M:
        return
    if copy_map[x][y]==6:
        return
    if copy_map[x][y]==0:
        copy_map[x][y]=-1
    check(x+dx,y+dy,dx,dy)


def play(x,y,n,d):
    if n==1:
        dx,dy=directions(n,d)
        check(x+dx,y+dy,dx,dy)
    else:
        for dx,dy in directions(n,d):
            check(x+dx,y+dy,dx,dy)


for i in range(N):
    n=list(map(int,input().split()))
    maps.append(n)
    for j in range(len(n)):
        map_info[n[j]].append((i,j))

copy_map=copy.deepcopy(maps)
result=10e5
ch_num=0
num=0
for i in range(1,5):
    if map_info[i]:
        num+=len(map_info[i])
cctv_case=list(product(range(4),repeat=num))




for w in range(len(cctv_case)):
    if map_info[5]:
        for i5 in range(len(map_info[5])):
            play(map_info[5][i5][0],map_info[5][i5][1],5,1)
    count=0
    for i in range(1,5):
        if map_info[i]:
            for j in range(len(map_info[i])):
                play(map_info[i][j][0],map_info[i][j][1],i,cctv_case[w][count])
                count+=1
    for i in range(N):
        for j in range(M):
            if copy_map[i][j]==0:
                ch_num+=1
    if result>ch_num:
        result=ch_num
    copy_map=copy.deepcopy(maps)
    ch_num=0



print(result)