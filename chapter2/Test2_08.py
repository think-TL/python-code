a_list = [1, 2, 3, 4, 5]

def sum_list(list01):
    count =0
    for i in list01:
        count +=i
    print count

    count = 0
    len01 = len(list01)
    flag = 0
    while len01 > 0:
        count +=list01[flag]
        flag +=1
        len01 -= 1
    print count

add = []
for i in range(5):
    add.append(int(raw_input("input number")))
sum_list(add)
