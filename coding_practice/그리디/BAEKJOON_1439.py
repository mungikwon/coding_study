a=input()
number0=0
number1=0

if a[0]=='0':
    number0=1
else:
    number1=1
for i in range(len(a)-1):
    if a[i]!=a[i+1]:
        if a[i+1]=='0':
            number0+=1
        else:
            number1+=1
if sum(list(map(int,a)))==0 or sum(list(map(int,a)))==len(a):
    print(0)
else:
    print(min(number0,number1))