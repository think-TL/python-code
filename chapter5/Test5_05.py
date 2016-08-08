def changes(money):
    money_list = [25, 10, 5, 1]
    count = 0
    for i in money_list:
        yushu = divmod(money, i)
        count += yushu[0]
        money = yushu[1]
    print "%d a %d cnets" %(count, money_list[money])

changes(74)