a=int(input("enter a number"))
r=a**0.5
count=0
if a==1:
   print("Not a prime")
elif a==2:
   print("prime")
for i in range(2,int(r+1)):
      if a%i==0:
         count=count+1
         break
if count==0:
         print("not prime")
else:
         print("prime")
