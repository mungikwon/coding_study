n=int(input())
n_list=list(map(int,input().split()))

max=n_list[0]
min=n_list[0]

for i in range(n):
    if n_list[i]>max:
        max=n_list[i]
    if n_list[i]<min:
        min=n_list[i]

print(max-min)
