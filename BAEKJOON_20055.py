
N,K=map(int,input().split())
belt=list(map(int,input().split()))
robot=[0]*2*N
result=0


def number2():
    for i in range(N-2,-1,-1):
        if robot[i]==1:
            if robot[i+1]==0 and belt[i+1]!=0:
                robot[i]=0
                robot[i+1]=1
                belt[i+1]-=1
        if robot[N-1]==1:
            robot[N-1]=0

def number3():
    if robot[0]==0 and belt[0]!=0:
        robot[0]=1
        belt[0]-=1

def number4():
    count=0
    for i in range(2*N):
        if belt[i]==0:
            count+=1
    if count>=K:
        return True
    return False



while(1):
    result+=1
    belt=belt[-1:]+belt[0:-1]
    robot=robot[-1:]+robot[0:-1]
    if robot[N-1]==1:
        robot[N-1]=0
    number2()
    number3()
    if number4()==True:
        break

print(result)
