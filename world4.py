'''
类型转换：
int()整数型
str()字符串型
float()浮点型
'''
#type() BIF是用来查看此变量属于什么类型例如：
a = '小甲鱼'

#打印出来的就会是str(),a的值属于str类型。其他以此类推
type(a)

#isinstance()是用来比较，是否属于此类型例如：
a = 555

#如果属于就会报ture不属于则报false。这里就是拿555与str比较，看555是否属于str类型，很显然不属于则报false
isinstance(a, str)