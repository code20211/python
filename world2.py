'''
if...else...循环条件判断
'''
#导入随机数字生成模块
import random

#将随机数字赋值给name
name = random.randint(1,3)

#生成一个
# 1.石头 
# 2.剪刀 
# 3.布 

#将用户的值赋给user_nuber
user_number = input("请输入一个值: 石头\n1. 剪刀\n2. 布\n3.")

#将输入的值转换为Int整数型
user_number = int(user_number)

#输出电脑出的数字
print(f"电脑出的是{name}")

# 做一个用户赢的判断
if name == user_number:
    print("平局!")
else:
    if user_number > name and not (user_number == 3 and name == 1):
        print("恭喜你赢了！")
    elif user_number == 1 and name == 3:
        print("恭喜你赢了！")
    else:
        print("很遗憾你,你输了！")


'''
list列表
'''
 ##  分别由数值'浮点数'字符串'布尔值类型
my_list = [11, 2.5, "中国", True]

print(my_list[0::-1])
##list列表中字符串是不可改变的，而数值类型是可以改变的,例如：

##查找list列表中的某一个元素：
my_list[0]        ## //[0],[1],[2],[3]list列表中查找某一个元素都是0开始，（查找倒数几位可以通过-1来查找）

my_list[2] = "6"   ##/是不可改变的
