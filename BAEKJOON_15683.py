from collections import deque
from itertools import combinations,product
import sys
import copy




input=sys.stdin.readline
N,M = map(int,input().split())
check_maps=[[0]*M for _ in range(N)]
maps=[]
cctv=[]
cctv5=[]
wall=[]

result=N*M

def cctv_check(i,j,k):
    if i<0 or i>=N or j<0 or j>=M or maps[i][j]==6:
            return 0
    check_maps[i][j]=1
    if k==0:
        cctv_check(i+1,j,k)
    if k==1:
        cctv_check(i-1,j,k)
    if k==2:
        cctv_check(i,j+1,k)
    if k==3:
        cctv_check(i,j-1,k)


def cctv1_check(i,j,k):
    cctv_check(i,j,k)

def cctv2_check(i,j,k):
    if k%2==0:
        cctv_check(i,j,0)  
        cctv_check(i,j,1)
    else:
        cctv_check(i,j,2)  
        cctv_check(i,j,3)

def cctv3_check(i,j,k):
    if k==0:
        cctv_check(i,j,1)  
        cctv_check(i,j,2)
    if k==1:
        cctv_check(i,j,1)  
        cctv_check(i,j,3)
    if k==2:
        cctv_check(i,j,0)  
        cctv_check(i,j,3)
    if k==3:
        cctv_check(i,j,0)  
        cctv_check(i,j,2)

def cctv4_check(i,j,k):
    if k==0:
        cctv_check(i,j,1)  
        cctv_check(i,j,2)
        cctv_check(i,j,3)
    if k==1:
        cctv_check(i,j,1)  
        cctv_check(i,j,3)
        cctv_check(i,j,0)
    if k==2:
        cctv_check(i,j,0)  
        cctv_check(i,j,3)
        cctv_check(i,j,2)
    if k==3:
        cctv_check(i,j,0)  
        cctv_check(i,j,2)
        cctv_check(i,j,1)


def cctv5_check(i,j):
    for k in range(4):
        cctv_check(i,j,k)      


for i in range(N):
    line=list(map(int,input().split()))
    for j in range(M):
        if line[j]!=0 and line[j]!=6 and line[j]!=5:
            cctv.append((i,j,line[j]))
        if line[j]==5:
            cctv5.append((i,j))
        if line[j]==6:
            wall.append((i,j))
    maps.append(line)

for i,j in cctv5:
    cctv5_check(i,j)
copy_map=copy.deepcopy(check_maps)

k_list=list(product([0,1,2,3],repeat=len(cctv)))

for lists in k_list:
    check_maps=copy.deepcopy(copy_map)
    for w in range(len(lists)):
        if cctv[w][2]==1:
            cctv1_check(cctv[w][0],cctv[w][1],lists[w])
        if cctv[w][2]==2:
            cctv2_check(cctv[w][0],cctv[w][1],lists[w])
        if cctv[w][2]==3:
            cctv3_check(cctv[w][0],cctv[w][1],lists[w])
        if cctv[w][2]==4:
            cctv4_check(cctv[w][0],cctv[w][1],lists[w])
    count=0
    for i in range(N):
        for j in range(M):
            if check_maps[i][j]==0:
                count+=1
    if result>count:
        result=count
result=result-len(wall)


print(result)

