from itertools import combinations

N=int(input())
maps=[]
X=[]
T=[]


def ck_look(x,y,direction):
    if direction==0:
        for i in range(x-1,-1,-1):
            if maps[i][y]=='S':
                return True
            if maps[i][y]=='O':
                return False
    if direction==1:
        for i in range(x,N):
            if maps[i][y]=='S':
                return True
            if maps[i][y]=='O':
                return False
    if direction==2:
        for i in range(y-1,-1,-1):
            if maps[x][i]=='S':
                return True
            if maps[x][i]=='O':
                return False
    if direction==3:
        for i in range(y,N):
            if maps[x][i]=='S':
                return True
            if maps[x][i]=='O':
                return False
    return False




def check():
    result=0
    for x,y in T:
        for i in range(4):
            if ck_look(x,y,i):
                return True
    return False


for i in range(N):
    line=list(input().split())
    for j in range(len(line)):
        if line[j]=='X':
            X.append((i,j))
        if line[j]=='T':
            T.append((i,j))
    maps.append(line)



find= False
for data in combinations(X,3):
    for x,y in data:
        maps[x][y]='O'
    if not check():
        find=True
        break
    for x,y in data:
        maps[x][y]='X'

    
if find:
    print("YES")
else:
    print("NO")
