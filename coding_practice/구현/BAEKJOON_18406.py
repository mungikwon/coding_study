score=input()

score1=score[0:int(len(score)/2)]
score2=score[int(len(score)/2):len(score)]

score1=map(int,score1)
score2=map(int,score2)

if sum(score1)==sum(score2):
    print("LUCKY")
else:
    print("READY")