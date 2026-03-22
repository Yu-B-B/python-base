# 方法定义方式1
def func1(num):
    if num % 2 == 0:
        return num * 3
    else:
        return num * 5


# 方法定义方式2
def func2(num: int, str_: str) -> int:
    if (str_.__eq__("shanzan")):
        return num * 3
    else:
        return num * 5


print(func1(5))
print(func2(4, 'shanzan'))


# 参数传递
# 1、必要传参。也成位置参数，定义的方法中有多少个参数，调用时需要按顺序传值，且不能缺失
def fun3(a, b):
    return a + b


print(fun3(4, 5))


# 2、关键字传参。定义的方法中存在参数名，调用时指定参数名传值，可忽略参数顺序
def fun4(a, b):
    return a - b


print(fun4(a=3, b=5))


# 3、默认值传参。定义方法时可指定某个参数存在默认值，调用时，可选择性是否为这个值传参，不传使用默认值，传了默认值被覆盖
def fun5(a, b, c=12):
    return a + b + c


print(f'默认值传参', fun5(4, 5, c=34))
print(f'默认值传参', fun5(4, 5))


# 4、不定长传参。定义参数可不用指定n个参数，调用时可传递足量数据
# *num, 表示不定长参数
# **args，表示不定长键值对
# 若有多种类型传参，参数顺序为，位置参数、默认参数、不定长参数、不定长关键字参数
result = 0
def fun6(a, b=10, *args, **kwargs):
    # 方法内部使用全局变量时，需要申明该变量是全局变量
    global result
    for arg in args:
        result = result + a + b + arg
    for k, v in kwargs.items():
        result = result + v
    return result


print(fun6(2, 4, 4, 4, 4, {'g': 1, 'h': 34}))


# 多参数返回，返回元组或分开获取
def fun7():
    return 10, 20


print(f'类型为：{type(fun7())}, 得到的值为:{fun7()}')
x, y = fun7()
print(x, y)
