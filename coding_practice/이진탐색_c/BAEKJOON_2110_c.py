N,C=map(int,input().split())
home=[]
for _ in range(N):
    home.append(int(input()))

home.sort()

min=home[1]-home[0]
max=home[len(home)-1]-home[0]
result=0


while(min<=max):
    value=home[0]
    mid=(max+min)//2
    count=1
    for i in range(1,len(home)):
        if home[i]>=mid+value:
            value=home[i]
            count+=1
    if count>=C:
        min=mid+1
        result=mid
    else:
        max=mid-1


print(result)