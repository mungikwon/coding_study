import collections


card=list(map(str,input().split()))
mincard=9999
card=collections.deque(card)
for _ in range(4):
    a=card.popleft()
    card.append(a)
    card1=''.join(card)
    card1=int(card1)
    if card1<mincard:
        mincard=card1

print(mincard)

cnt=0
for i in range(1,10,1):
    for j in range(1,10,1):
        for k in range(1,10,1): 
            for l in range(1,10,1):    
                go=i*1000+j*100+k*10+l
                cnt+=1
                if go==mincard:
                    result=cnt

print(result-1)
