room=[[0]*100 for _ in range(100)]
result=0
for i in range(4):
    a,b,c,d=map(int,input().split())
    for j in range(a,c):
        for k in range(b,d):
            room[k][j]=1

for i in range(100):
    for j in range(100):
        if room[i][j]==1:
            result=result+1

print(result)





""" 
room=[[0]*100 for _ in range(100)]

for _ in range(4):
    a,b,c,d=map(int,input().split())
    for j in range(a,c):
        for k in range(b,d):
            room[j][k]=1

answer=0
for row in room:
    answer += sum(row)
print(answer)
     """
