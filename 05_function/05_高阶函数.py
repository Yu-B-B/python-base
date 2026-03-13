# 把函数作为参数传递
# 函数的参数是函数

def fun1(a=0):
    return abs(a)


def fun2(c, d, method):
    return method(c) + method(d)


# 使用fun1()表示是将方法的返回结果作为参数传递，在方法内部调用时，翻译出来就是想在常量上调用函数
# print(fun2(-3, -5, fun1()))

# 正确的调用方式为
print(fun2(-4, -5, fun1))


# 2、函数的返回值为函数
def fun3(*args):
    def fun3_1():
        a = 0
        for arg in args:
            a += arg
        return a

    return fun3_1


print(fun3(1, 2, 3))
print(fun3(1, 2, 3)())
