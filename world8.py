#函数

#函数是以def开头定义    设置方法名：MyFuncotuion()   一定要加括号，括号内是形参可以多个，一般位2-4个
def MyFuncotuion():
    print('hello!')

#调用MyFuncotuion()方法，直接将方法名字调用即可
MyFuncotuion()



#global  将局部变成全局

cout = 6

def hello():
    # global cout
    cout = 10
    print(cout)

hello()
print(cout)


def hhhx(x):
    def gggy(y):
        return x * y

    return hhhx


hhhx(5)(8)