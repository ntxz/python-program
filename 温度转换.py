tempstr=input("请输入带单位的温度：")
if tempstr[-1] in ['F','f']:
    C=(eval(tempstr[0:-1])-32)/1.8
    print("装换后的温度为{:.2f}C".format(C))
elif tempstr[-1] in ['C','c']:
    F=1.8*eval(tempstr[0:-1])+32
    print("装换后的温度为{:.2f}F".format(F))
else:
    print("输入错误")
