from itertools import permutations

N=int(input())
numbers=list(map(int,input().split()))
cal=list(map(int,input().split()))
cals=[]
mins=1e9
maxs=-1e9

def cal_num(A):
    result=numbers[0]
    for i in range(len(A)):
        if A[i]==0:
            result=result+numbers[i+1]
        if A[i]==1:
            result=result-numbers[i+1]
        if A[i]==2:
            result=result*numbers[i+1]
        if A[i]==3:
            if result<0:
                result=(result*-1)//numbers[i+1]
                result=result*-1
            else:
                result=result//numbers[i+1]
    return result

for i,j in enumerate(cal):
    if i==0:
        for _ in range(j):
            cals.append(0)
    if i==1:
        for _ in range(j):
            cals.append(1)
    if i==2:
        for _ in range(j):
            cals.append(2)
    if i==3:
        for _ in range(j):
            cals.append(3)

for A in list(permutations(cals,N-1)):
    cal_r=cal_num(A)
    if cal_r<mins:
        mins=cal_r
    if cal_r>maxs:
        maxs=cal_r

print(maxs)
print(mins)