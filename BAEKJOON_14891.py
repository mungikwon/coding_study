import copy

wheel=[]
def check(N,D,R_L):
    Direction[N]=D
    if R_L=='L' and N==0:
        return
    if R_L=='R' and N==3:
        return
    if R_L=='L':
        if wheel[N][6]==wheel[N-1][2]:
            return
        if wheel[N][6]!=wheel[N-1][2]:
            return check(N-1,D*-1,'L')
    if R_L=='R':
        if wheel[N][2]==wheel[N+1][6]:
            return
        if wheel[N][2]!=wheel[N+1][6]:
            return  check(N+1,D*-1,'R')

wheel_copy=[]
def change():
    wheel_copy=copy.deepcopy(wheel)
    for i in range(4):
        if Direction[i]==1:
            for j in range(8):
                wheel[i][j]=wheel_copy[i][(j-1)%8]
        if Direction[i]==-1:
            for j in range(8):
                wheel[i][j]=wheel_copy[i][(j+1)%8]


def score():
    result=0
    for i in range(4):
        if wheel[i][0]=='1':
            result+=2**i
    return result


for i in range(4):
    wheel.append(list(input()))

K=int(input())

for _ in range(K):
    N,D =map(int,input().split())
    Direction=[0]*4
    check(N-1,D,'R')
    check(N-1,D,'L')
    change()
    print(Direction)
    print(wheel)

print(score())








    
