import heapq

N=int(input())

card=[]
result=0

for _ in range(N):
    heapq.heappush(card,int(input()))


while len(card)!=1:
    a=heapq.heappop(card)
    b=heapq.heappop(card)
    result+=a+b
    heapq.heappush(card,a+b)

print(result)

