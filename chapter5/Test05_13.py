def tominu(str):
    lis = str.split(":")
    a = int(lis[0]*60)
    print a
    b = int(lis[1])
    return a+b
print tominu("5:1")