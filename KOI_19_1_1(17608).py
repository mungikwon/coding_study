N=int(input())
bar_list=[]
result=0
size=0

for _ in range(N):
    a=int(input())
    bar_list.append(a)


for k in range(len(bar_list)):
    a=bar_list.pop()
    if a>size:
        size=a
        result+=1
print(result)