a = int(raw_input("input number"))
b = int(raw_input("input number"))
c = int(raw_input("input number"))
if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b
print a, b, c

if a < b:
    a, b = b, a
if a < c:
    a, c = c, a
if b < c:
    b, c = c, b
print a, b, c


