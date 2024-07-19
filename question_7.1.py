'''
you are given space separated list
find no of even and odd elements in a given list


'''
n=list(map(int,input().split(" ")))
even=0
odd=0
for i in range(0,len(n)):
    if(n[i]%2==0):
        even+=1
    else:
        odd+=1
print(even,odd)
       

   

