# num1=2
# num2=5
# print(num1+num2)


# n1=int(input("enter first number"))
# n2=int(input("enter second number"))
# print(n1+n2)

# n3=int(input("enter first number"))
# n4=int(input("enter second number"))
# print(n3-n4)

# n3=int(input("enter first number"))
# n4=int(input("enter second number"))
# print(n3**n4)


# n3=int(input("enter first number"))
# n4=int(input("enter second number"))
# print(n3*n4)

# n3=int(input("enter first number"))
# n4=int(input("enter second number"))
# print(n3/n4)

'''
logical 
 and && 
 or ||






'''
# a=3
# b=2
# print(a & b)

# age=25
# if(age>=18 and age<24):
#     print("only two wheelers")
# elif(age>=24 and age<45):
#     print("two and four wheelers")
# else:
#     print("all")


# age=int(input("enter age"))
# if(age>=18 and age<24):
#     print("only two wheelers")
# elif(age>=24 and age<45):
#     print("two and four wheelers")
# elif(age<18):
#     print("kids")  
# else:
#     print("all")



'''
person x goes to market  buys 10 apples, 2 dozen bananas,8 oranges
cost of 1 apple is 15rs
cost of 1banana is 4
1 orange is 5rs







'''

# n=int(input("how much you have"))
# apple=int(input("no of apples"))
# banana=int(input("no of bananas"))
# orange=int(input("no of oranges"))
# sum=(apple*15)+(banana*4)+(orange*5)
# if(sum<n):
#     print("not cheated")
# else:
#     print("cheated")



# n=int(input("enter number"))
# if(n%2==0 and n>0):
#     print("even positive")
# elif(n%2==0 and n<0):
#     print("even negative")
# elif(n%2!=0 and n>0):
#     print("odd positive")
# else:
#     print("odd negative")

# n=20
# if(n%2==0 and n>0):
#     print("even positive")
# elif(n%2==0 and n<0):
#     print("even negative")
# elif(n%2!=0 and n>0):
#     print("odd positive")
# else:
#     print("odd negative")


# h=int(input("enter height"))
# w=int(input("enter weight"))
# f=int(input("enter bodyfat"))
# if(h>140 and w%2==0 and f<=12):
#     print("you are eligible")
# else:
#     print("not eligible")
#     x=True
#     y=False


# h1=int(input("enter height"))
# w1=int(input("enter weight"))
# f1=int(input("enter bodyfat"))
# if(h1>118 and h1<148 and w1%7==0):
#     print("eligible")
# else:
#     print("not eligible")
#     x=True
#     y=False
#     if(x==y):
#         print("they are in the same flight")
#     else:
#         print("not in the same flight")





#SUM OF FIRST N NATURAL NUMBERS
# n=int(input("enter a number"))
# sum=n*(n+1)/2
# print(sum)

'''
this is not the efficient way

'''
# n=int(input("enter a number"))
# for i in range(2,n):
#     if(n%i==0):
#         print("not a prime")
#         break
# else: #else for for not for if
#     print("prime")


     # ardam kani code   
# count=0
# n=int(input("enter number"))
# for i in range(1,n+1):
#     if n%i==0:
#         count+=1
# if count==2:
#     print("prime")
# else:
#     print("not prime")

import math
n=int(input("enter a number:"))
sq=int(math.sqrt(n))
i=2
while i<=sq:
    if sq%i==0:
        break
    i=i+1
if i==sq:
    print("square root of a number is prime number")   
else:
    print("square root of a number is not a primenumber")
        
        
        
        
       











