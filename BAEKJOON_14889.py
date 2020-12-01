from itertools import combinations
import copy

N=int(input())
S=[list(map(int,input().split())) for _ in range(N)]

people=[]
result=10e5
for i in range(N):
    people.append(i)

cases=list(combinations(people,int(N/2)))

for case in cases:
    team1=0
    team2=0
    case2=[]
    for i in people:
        if i not in case:
            case2.append(i)

    for i in case:
        for j in case:
            team1+=S[i][j]
   
    for i in case2:
        for j in case2:
            if S[i][j]!=0:
                team2+=S[i][j]
    
    if result>abs(team1-team2):
        result=abs(team1-team2)

print(result)


