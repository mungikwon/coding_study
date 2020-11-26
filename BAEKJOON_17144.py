import copy 

R,C,T=map(int,input().split())
maps=[]
item_lo=[]
result=0
for i in range(R):
    row=list(map(int,input().split()))
    if row[0]==-1:
        item_lo.append(i)
    maps.append(row)



dx=[-1,1,0,0]
dy=[0,0,-1,1]

def spread():
    new_maps=[[0]*C for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if maps[i][j]==0 or maps[i][j]==-1:
                continue
            check_room=0
            for k in range(4):
                x=i+dx[k]
                y=j+dy[k]
                if x<0 or y<0 or x>=R or y>=C or maps[x][y]==-1:
                    continue
                check_room+=1
                new_maps[x][y]+=maps[i][j]//5
            new_maps[i][j]+=(maps[i][j]-(maps[i][j]//5)*check_room)
            new_maps[item_lo[0]][0]=-1
            new_maps[item_lo[1]][0]=-1
    return new_maps

def work():
    copy_maps=copy.deepcopy(maps)
    copy_maps[item_lo[0]][0]=0
    for i in range(1,C):
        maps[item_lo[0]][i]=copy_maps[item_lo[0]][i-1]
    for i in range(item_lo[0]-1,-1,-1):
        maps[i][C-1]=copy_maps[i+1][C-1]
    for i in range(C-2,-1,-1):
        maps[0][i]=copy_maps[0][i+1]
    for i in range(1,item_lo[0]):
        maps[i][0]=copy_maps[i-1][0]
    maps[item_lo[0]][0]=-1
    copy_maps[item_lo[1]][0]=0
    for i in range(1,C):
        maps[item_lo[1]][i]=copy_maps[item_lo[1]][i-1]
    for i in range(item_lo[1]+1,R):
        maps[i][C-1]=copy_maps[i-1][C-1]
    for i in range(C-2,-1,-1):
        maps[R-1][i]=copy_maps[R-1][i+1]
    for i in range(R-2,item_lo[1]-1,-1):
        maps[i][0]=copy_maps[i+1][0]
    maps[item_lo[1]][0]=-1


 


for _ in range(T):
    maps=spread()
    work()


for i in range(R):
    for j in range(C):
        if maps[i][j]!=-1:
            result+=maps[i][j]

print(result)