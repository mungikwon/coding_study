import sys
from itertools import product
import copy
input=sys.stdin.readline


N=int(input())
maps=[list(map(int,input().split())) for _ in range(N)]


def change(lists):
    new_list=[[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_list[i][j] = lists[j][i]
    return new_list

def play(maps,n):
    new_maps=[]*N
    if n==1:
        for i in range(N):
            new_maps.append(line_play(maps[i]))
        return new_maps
    if n==2:
        for i in range(N):
            maps[i].reverse()
            new_maps.append(line_play(maps[i]))
        for i in range(N):
            new_maps[i].reverse()
        return new_maps
    if n==3:
        maps=change(maps)
        for i in range(N):
            new_maps.append(line_play(maps[i]))
        new_maps=change(new_maps)
        return new_maps

    if n==4:
        maps=change(maps)
        for i in range(N):
            maps[i].reverse()
            new_maps.append(line_play(maps[i]))
        for i in range(N):
            new_maps[i].reverse()
        new_maps=change(new_maps)
        return new_maps    

def line_play(k):
    a=[0]*len(k)
    result=[]
    for i in range(len(k)-1):
        for j in range(i+1,len(k)):
            if k[j]!=0 and k[j]!=k[i]:
                break
            if k[i]!=0 and k[i]==k[j]:
                a[i]=k[i]+k[j]
                k[i]=0
                k[j]=0
                break
    for i in range(len(k)):
        if a[i]!=0:
            result.append(a[i])
        elif k[i]!=0:
            result.append(k[i])
    for _ in range(len(k)-len(result)):
        result.append(0)
    return result





prod=list(product([1,2,3,4],repeat=5))
result=0
copy_map=copy.deepcopy(maps)
for k in prod:
    maps=copy.deepcopy(copy_map)
    for l in k:
        maps=play(maps,l)
    for i in range(N):
        for j in range(N):
            if maps[i][j]>result:
                result=maps[i][j]
print(result)