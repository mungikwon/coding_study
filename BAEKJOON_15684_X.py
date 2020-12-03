import copy
from itertools import combinations 
N,M,H= map(int,input().split())
rmaps=[[0]*N for _ in range(H)]
find_index=[]
maps=[]
# for i in range(H):
#     for j in range(0,N-1):
#         find_index.append((i,(j,j+1)))
#     find_index.remove((i-1,(j-1,j)))
#     find_index.remove((i-1))



def find_point():
    for i in range(H):
        for j in range(0,N-1):
            if maps[i][j]==0 and maps[i][j+1]==0:
                find_index.append((i,j))

def check():
    result=[0]*N
    for j in range(N):
        i=0
        index=j
        while(1):
            if maps[i][index]==1:
                if index>0 and maps[i][index-1]==1:
                    index-=1
                elif index<=N-1 and maps[i][index+1]==1:
                    index+=1
            i+=1
            if i==H:
                if j!=index:
                    return False
                break
    return True

def play():
    if check()==True:
        return 0
    maps=rmaps
    for x,y in find_index:
        maps[x][y]=1
        maps[x][y+1]=1
        if check()==True:
            return 1
        maps[x][y]=0
        maps[x][y+1]=0

    for i in range(2,4):
        cases=combinations(find_index,i)
        cases=list(cases)
        if len(find_index)==i:
                cases=cases[0]
        print("casese1",cases)
        for case in cases:
            for j in range(len(case)-1):
                if case[j][0]==case[j+1][0] and abs(case[j][1]-case[j+1][1])==1:
                    print(case)
                    print("1",cases)
                    cases.remove(case)
                    print("2",cases)
                    break
        print("cases2",cases)
        for case in cases:
            for x,y in case:
                maps[x][y]=1
                maps[x][y+1]=1

            if check()==True:
                return i

            for x,y in case:
                maps[x][y]=0
                maps[x][y+1]=0
    return -1

for _ in range(M):
    i,j = map(int,input().split())
    rmaps[i-1][j-1]=1
    rmaps[i-1][j]=1

maps=copy.deepcopy(rmaps)
find_point()
print(play())

# find_point()
# print(find_index)