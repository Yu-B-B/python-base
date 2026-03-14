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

# 3、map函数，接受一个函数和多个可迭代对象，再将对象中每一个元素处理后返回迭代器
# 普通函数方式：
numbers = [1, 2, 4, 5, 6, 7]


def fun4(a):
    return a * a


print(f'普通函数调用方法后：{map(fun4, numbers)}')
print(f'普通函数调用方法,转为数据后：{list(map(fun4, numbers))}')

# map高阶
map_result = map(lambda a: a ** 2, numbers)
print(f'python内置函数调用后{list(map_result)}')
