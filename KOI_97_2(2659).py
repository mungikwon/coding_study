import collections


card=list(map(str,input().split()))
card_list=[0]*10000
def play(a):
    mincard=9999
    card=collections.deque(a)
    for _ in range(4):
        a=card.popleft()
        card.append(a)
        card1=''.join(card)
        card1=int(card1)
        if card1<mincard:
            mincard=card1
    return mincard

mincard=play(card)



cnt=0
for i in range(1,10,1):
    for j in range(1,10,1):
        for k in range(1,10,1): 
            for l in range(1,10,1):    
                go=i*1000+j*100+k*10+l
                if card_list[play(str(go))]==0:
                   card_list[play(str(go))]=1
                   cnt+=1
                if go==mincard:
                    result=cnt

print(result)


""" 
def find_num(num):
    result=num
    for _ in range(3):
        num = (num%1000)*10 +num//1000
        if result>num:
            result=num
    return result

card=find_num(int(''.join(input().split())))

i=1111
cnt=0
while(i<=card):
    if find_num(i)==i:
        cnt+=1
    i+=1
print(cnt) """

