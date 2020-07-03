room=[[] for _ in range(10)]

nx=[0,-1,0,1]
ny=[-1,0,1,0]
lo=[]

def check(y,x):
    result=0
    for k in range(4):
        dx=x+nx[k]
        dy=y+ny[k]
        if room[dy][dx]==0:
            result+=1

    if result==3:
         lo.append([y+1,x+1])       


for i in range(10):
    room[i]=list(map(int,input()))


for i in range(10):
    for j in range(10):
        if room[i][j]==1:
            check(i,j)


if len(lo)==2:
    lo.append([lo[0][0],lo[1][1]])

lo.sort()

for 

if len(lo)==3:
    print(lo)
else:
    print("0")
