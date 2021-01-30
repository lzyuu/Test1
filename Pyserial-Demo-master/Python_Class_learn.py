'''

类把数据与功能绑定在一起。创建新类就是创建新的对象 类型，
从而创建该类型的新 实例 。类实例具有多种保持自身状态的属性。
类实例还支持（在类中定义的）改变自身状态的方法。


有没有可能搞一个超线程的串口工具
Class serial()
    theading += 1

一次性跑 16 个串口

'''


'''
先从头开始学习一下
'''

def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)


class MyClass:
    """A simple example class"""
    i = 12345
    def __init__(self):
        self.data = []
    def f(self):
        return 'hello world'


x = MyClass()
