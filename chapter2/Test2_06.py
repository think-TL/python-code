try:
    int01 = int(raw_input("input int"))
    if int01 > 0:
        print "int01>0"
    elif int01 ==0:
        print "int01 is 0"
    else:
        print "int01 < 0 "
except ValueError:
    print "user input error"