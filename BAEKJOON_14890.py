import sys
input=sys.stdin.readline

N,L=map(int,input().split())
maps=[]
line=[]
for i in range(N):
    A=list(map(int,input().split()))
    line.append(A)
    maps.append(A)
for j in range(N):
    A1=[]
    for i in range(N):
        A1.append(maps[i][j])
    line.append(A1)



def check(a):
    lens=1
    N=len(a)
    for i in range(1,N):
        if abs(a[i]-a[i-1])>1:
            return -1
        if a[i-1]==a[i]:
            lens+=1
        if a[i]-a[i-1]>0:
            if lens<L:
                return -1
            if lens>=L:
                    lens=1
        if a[i]-a[i-1]<0:
            if lens<0:
                return -1
            lens=-L+1 
    if lens<0:
       return -1
    return 1




result=0
for a in line:
    if check(a)==1:
        result+=1

print(result)
