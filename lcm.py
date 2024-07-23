import math
a=int(input("enter 1st number: "))
b=int(input("enter 2nd number: "))
lcm=a*b//gcd
gcd = math.gcd(a, b)
print("lcm of two numbers:",lcm)