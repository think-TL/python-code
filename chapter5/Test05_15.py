def least_multiple(x, y):
   if x > y:
        greater = x
   else:
        greater = y
   while(True):
        if((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1
   return lcm

num1 = int(input("Enter num1"))
num2 = int(input("Enter num2"))
print( num1,"and", num2,"Least common multiple", least_multiple(num1, num2))

def hcf(a,b):
    if a<b:
        a,b=b,a
    while b != 0:
        temp = a%b
        a=b
        b=temp
    return a

num1 = int(input("Enter num1"))
num2 = int(input("Enter num2"))
print( num1,"and", num2,"Greatest common divisor", hcf(num1, num2))