#while循环,条件满足就执行下面的任务不满足就重复知道满足设定的条件
zqda = '漫橘长'#设定一个正确答案


# 课程已经学习到第10讲



name = input('请输入姓名：')#提示用户输入正确答案

while True:#当条件为真时执行下面code

    if name == zqda:

        break  #符合条件时跳出循环体

    name = input('抱歉。错误，请重新输入:')

print('哎哟！帅哦。')
print('你真是漫橘长心中的蛔虫！')


#for 循环没懂，后续补


#了不起的循环
age = input('请输入你的成绩')
samll = int(age)
if 100>= samll >=80:
    print('成绩优秀！')
elif 80>= samll >=60:
    print('及格！')
elif 60>= samll >= 0:
    print('不及格')
elif samll<=0:
    print('请输入合法数值')
