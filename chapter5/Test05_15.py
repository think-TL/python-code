def lcm(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        temp = a % b
        a = b
        b = temp
    return a

num1 = int(input("Enter num1"))
num2 = int(input("Enter num2"))
print( num1,"and", num2,"Least common multiple", lcm(num1, num2))

num1 = int(input("Enter num1"))
num2 = int(input("Enter num2"))
print lcm(num1,num2)
print( num1,"and", num2,"Greatest common divisor", (num1*num2)/lcm(num1, num2))
