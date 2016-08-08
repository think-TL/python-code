#-*- coding: UTF-8 -*-
def rate_of_return(rate):
    print "年回报率为：%f" %(10000.00*rate*365/10000.00)
rate=raw_input("请输入存款利率")
rate=float(rate)
rate_of_return(rate)