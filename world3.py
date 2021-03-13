import random#导入random随机数值模块

# ==(等于)  !=(不等于)  >   <   +  -  /  *  and（两边同时正确，有一个不满足将得到false）




scrrl = random.randint(1,10)#生成一个1~10之间的随机数值存入scrrl中

temp = input('请输入小甲鱼的新中国数值：')

guess = int(temp)

while guess != scrrl: #循环语句，只要用户输入的数值不等于scrrl就一直执行下面的任务直到等于随机数

    temp = input('输入错了，请输重新输入小甲鱼的心中数值：') #将用户输入的值存入temp中

    guess = int(temp) #转换整形    数值型

    if guess == scrrl:  #设置条件 如果符合条件执行下面两条不符合执行else中任务
        print('你真是小甲鱼心中的蛔虫!')
        print('哼,猜中了也没有奖励！')
    else: 
        if guess > scrrl:
            print('哥，大了大了~')
        else:
            print('嘿！小了小了！')

print('游戏结束！不玩了！')