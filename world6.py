#列表 
# 数组[]中可以添加任何元素包括列表、对象，但c语言、JavaScript哪些不行！
#例如：
meber = ['黑夜','漫橘长',3.25,[1,2,3]]
print(meber)

#向列表添加元素
#添加方法：.append()   
# 同时添加连个：.extend([''])必须以数组形式添加记得加[]有连个参数所以必须填入连个参数
# 按顺序添加一个参数.insert()
#例如：  这里是将hello字符串添加到列表的地四位（编程中列表第一位都是从0开始数）
meber.insert(4,'Hello')
print(meber)

#例如：
meber.append('葫芦娃')   #‘append()’  方法使用
len(meber)    #检查列表长度：‘len'
print(meber)

#range()   快速生成指定范围的列表方法
l3 = list(range(50))
print(l3)


#删除列表元素  
#.remove('')不需要知道这个元素在列表什么位置只需知道这个元素存在这个列表中即可
meber.remove('漫橘长')
print(meber)

#del  不是一个方法，它是一个语句，可以删除任意元素也可以直接将列表删除
del meber[1]#将列表第二个元素删除
print(meber)

#.pop()  删除列表中某个元素并且打印出删除的元素
meber.pop(1)
print(meber)

#.count( )    计算一个元素在列表中出现的次数或是有几个
meber.count('漫橘长')   

#.index()    计算一个元素在列表中的位置
#如果列表出现多个一样的要找位置   设置一个范围: .index('漫橘长',起始位,结束位)
meber.index('漫橘长')
meber.index('漫橘长',3,8)

#.reverse()  不需要参数   将列表反转，大的跑到列表最后小的跑到列表最前
meber.reverse()

#.sort()不需要参数情况下:  默认从小到大排序
meber = [1,3,3,7,5,9]
meber.sort()
#输出的列表位：[1,3,3,5,7,9]




#列表分片    [此处是索引 起始值   :   此处是索引 结束值]    起始值不填默认从0位开始   结束值不填默认从末端开始   都不填将不变
meber = [123,'黑夜','小布丁',8.454]
meber[1:4]  #我想取“  '黑夜','小布丁',8.454 ”几个值
meber[:3]
meber[:]  

naber = meber[:]    #将meber列表值赋值给naber
naber1 = naber      #58-59性质是不一样的，58是将列表拷贝了一份就相当于有两份，而59是将58的值赋值给了59，如果修改59的内容59也会随着改变
print(naber)


#列表比较   
#这里比较时，列表比较都是比较起始位，如果起始位赢了后面的就不用比较了
#列表之间可以用 拼接字符串来拼接  例如： list_4 = list_1 + list_2  得到的结果就会是：list_4 = [123,233,442,111]
list_1 = [123,233]
list_2 = [442,111]
list_1 > list_2 