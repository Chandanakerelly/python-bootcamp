'''
method of list
append
insert
pop
slicing
reverse
sort
copy
remove
clear
length

aggregrate functions
sum
min
max
average

'''
# a=[1,2,3,4,-4,-9]
# a.append(99)
# a.insert(0,6)
# print(len(a))
# a.pop(0) #without giving any specific index last index is eliminated
# b=[7,8,9]
# c=a+b
# b=a.copy()
# print(*b)
# a.clear()
# print(*a) #* is used to remove comma 
# cnt=a.count(2)
# print(cnt)
# a.sort()
# a.pop()
# a.pop(2)
# print(*a)

'''
dynamic list

'''

# my_list=list(map(str,input().split(",")))
# print(*my_list)

# c=["chandu","mayu","nandu"]
# c.append("soumi")
# cnt=c.count("mayu")
# print(cnt)
# print(*c)


# a=list(map(str,input().split(",")))
# a.append("soumi")
# a.pop(2)
# a.pop()
# print(*a)


# append=1,pop=2,sort=3 ,4=length

a=list(map(int,input().split(",")))
print("enter 1 to append")
print("enter 2 to pop")
print("enter 3 to sort")
choice=int(input("enter the choice: "))
if(choice==1):
   a.append(2)
   print(*a)
elif(choice==2):
    print("pop")
elif(choice==3):
     print(sort)
elif(choice==4):
    print("length")
