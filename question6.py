'''

count odd elements

take  a space separated input from user and print alternate elements






'''

n=list(map(int,input().split()))
for i in range(0,len(n),2):
    print(n[i],end="")