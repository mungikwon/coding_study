import copy

N,K= map(int,input().split())
belt=list(map(int,input().split()))
robot=[0]*2*N



def number_1():
    belt_copy=copy.deepcopy(belt)
    robot_copy=copy.deepcopy(robot)
    for i in range(2*N):
        belt[(i+1)%(2*N)]=belt_copy[i]
        robot[(i+1)%(2*N)]=robot_copy[i]
    print("n1",robot)
    print("n1",belt)
    

def number_2(): #첫시작일때는 작동되면안댐
    n=0
    robot_index=0

    for i in range(2*N):
        if robot[i]==2:
            robot_index=i
            break

    while(n<(2*N-1)):
        if robot_index==N:
            robot[robot_index]=0
            continue

        if robot[(robot_index+1)%(2*N)]==0:
            if robot[robot_index%(2*N)]==1 or robot[robot_index%(2*N)]==2:
                if belt[(robot_index+1)%(2*N)]>=1:
                    robot[(robot_index+1)%(2*N)]=robot[robot_index%(2*N)]
                    robot[(robot_index)%(2*N)]=0
                    belt[(robot_index+1)%(2*N)]-=1

        n+=1
        robot_index-=1
    print("n2",robot)

    print("n2",belt)
    
def number_3(result):
    if result==1:
        robot[0]=2
        belt[0]-=1
    else:
        if robot[0]==0:
            robot[0]=1
            belt[0]-=1

def number_4():
    n=0
    for i in range(2*N):
        if belt[i]<=0:
            n+=1
    if n>=K:
        return True
    return False



result=1

while(1):

    number_1()
    number_2()
    number_3(result)
    print("result_r",result,robot)
    print("result_b",result,belt)
    if number_4()==True:
        print(result)
        break
    result+=1



