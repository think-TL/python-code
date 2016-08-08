#-*- coding: UTF-8 -*-
for i in range(0,21):
    if i % 2 == 0:
        print i,
print
print "================"
for i in range(0,21):
    if i % 2 != 0:
        print i,

"""是否被2整除"""

print
def is_div_by(x, y):
    if float(x) % float(y) == 0:
       return 1
x = raw_input("input number")
y = raw_input("input number")
if is_div_by(x, y) == 1:
    print "整除"
else:
    print "no"