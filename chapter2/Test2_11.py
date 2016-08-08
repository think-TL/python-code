def general(general):
    add = []
    for i in range(5):
        add.append(int(raw_input("input number")))
    count = 0
    for i in add:
        count += i
    if general == 1:
        print count
    else:
        print float(count) / len(add)


while True:
    print "five--sum --1"
    print "five--avg --2"
    print "break --X"
    try:
        sel = int(raw_input("Please select a"))
        if sel == 1:
            general(1)
        elif sel == 2:
            general(2)
        else:
            print "input error"
    except ValueError:
        break
