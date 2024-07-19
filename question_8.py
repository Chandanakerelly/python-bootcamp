'''
given an ss integer list find the average of elements present in the even index



'''


n=list(map(int,input().split(" ")))
sum=0
c=len(n)
for i in range(len(n)):
    if(i%2==0):
        sum+=n[i]
print(sum/c)
        
        







