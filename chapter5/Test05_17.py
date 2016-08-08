import random
n = random.randint(1, 101)
N = range(n)
for i in range(n):
    N[i] = random.randint(0, 2**31)
print n
N.sort()
print N