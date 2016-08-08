while True:
    try:
        num = int(raw_input("please input one value (1-100)"))
        num_list = [i for i in range(1, 101)]
        if num in num_list:
            print num
            break
    except ValueError:
        print "error"
