string01 = raw_input("input string")
print string01

try:
    int01 = int(raw_input("input int"))
    print int01
except ValueError:
    print "user input error"