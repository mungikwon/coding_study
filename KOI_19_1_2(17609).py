

def check(w):
    st=0
    la=len(w)-1
    while(st!=round(len(a)/2)):
        if w[st]!=w[la]:
            return 2
        st+=1
        la-=1
    return 1

N=int(input())



for i in range(N):
    a=input()
    st=0
    la=len(a)-1
    find_index=[]
    while(st!=round(len(a)/2)):
        if a[st]!=a[la]:
            find_index.append([st,la])
            break
        st+=1
        la-=1 

    result=0


    if find_index:
        index1,index2=find_index[0]
        a1=a[:index1]+a[index1+1:]
        a2=a[:index2]+a[index2+1:]
        if check(a1)==1 or check(a2)==1:
            result=1
        else:
            result=2

    else:
        result=0

    print(result)
    
            





