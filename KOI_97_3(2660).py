import collections

N=int(input())
a=N
people=[[] for _ in range(N+1)]




# def paly(a):
#     check=[0]*(N+1)
#     count=0
#     q=collections.deque()


        





while(a!=-1):
    a,b=map(int,(input().split()))
    if (a!=-1):
        people[a].append(b)
        people[b].append(a)
print(people)
print(people[2])