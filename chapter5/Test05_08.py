#-*- coding: UTF-8 -*-
graph = raw_input("请输入你要计算的几何种类（A.正方形，B立方体，C圆，D球）：")

if graph == "A":
    b = raw_input("请输入正方形的边长： ")
    a = float(b)
    print "正方形的面积为：%f" %(a**2)
elif graph == "B":
    b = raw_input("请输入正方体的边长： ")
    a = float(b)
    print "正方体的面积为：%f" %(a**2*6)
elif graph == "C":
    b = raw_input("请输入圆的半径： ")
    a = float(b)
    print "圆的面积为：%f" %(3.14*a**2)
elif graph == "D":
    b = raw_input("请输入球的半径： ")
    a = float(b)
    print "球的面积为：%f" %(4*3.14*a**2)
else:
    print "你输入的几何种类错误，请重新运行程序重新输入"