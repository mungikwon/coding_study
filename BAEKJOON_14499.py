import copy
from collections import deque

N,M,x,y,K=map(int,input().split())
maps=[]
dice=[[-1,2,-1],[4,1,3],[-1,5,-1],[-1,6,-1]]
change=[]

print(dice)

dx=[0,1,0,-1]
dy=[1,0,-1,0]

def change_dice(i):
    dice_copy=copy.deepcopy(dice)
    if i ==1:
        dice[1][2]=dice_copy[1][1]
        dice[1][1]=dice_copy[1][0]
        dice[1][0]=dice_copy[3][1]
        dice[3][1]=dice_copy[1][2]
    if i==2:
        dice[1][1]=dice_copy[1][2]
        dice[1][0]=dice_copy[1][1]
        dice[3][1]=dice_copy[1][0]
        dice[1][2]=dice_copy[3][1]
    if i==3:
        for w in range(4):
            dice[(w+1)%4][1]=dice_copy[w][1]
    if i==4:
        for w in range(4):
            dice[(w-1)%4][1]=dice_copy[w][1]
    print(dice)

change_dice(1)
change_dice(4)

# for i in range(N):
#     lists=list(map(int,input().split()))    
#     maps.append(lists)

# order=list(map(int,input().split()))

# print(maps)

for i in order:
    x=x+dx[i]
    y=y+dy[i]
    if x<0 or y<0 or x>=N or y>=M:
        x=x-dx[i]
        y=y-dy[i]
        continue
    change_dice(i)
    if maps[x][y]==0:
        maps[x][y]=dice[3][1]
    elif maps[x][y]!=0:
        dice[3][1]=maps[x][y]
        maps[x][y]=0
    print(maps[1][1])
        


